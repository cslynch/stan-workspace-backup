/**
 * Search Logger Wrapper
 * Logs all web_search tool calls with metadata (timestamp, provider, query, source)
 * Enforces 2-second delay between consecutive Brave Search calls
 * Writes to /workspace/research/search-log.jsonl
 */

const fs = require('fs');
const path = require('path');

const SEARCH_LOG_PATH = path.join(
  process.env.HOME || '/home/clawdbot',
  '.openclaw/workspace/research/search-log.jsonl'
);

const RESEARCH_DIR = path.dirname(SEARCH_LOG_PATH);

// Ensure research directory exists
if (!fs.existsSync(RESEARCH_DIR)) {
  fs.mkdirSync(RESEARCH_DIR, { recursive: true });
}

let lastBraveSearchTime = 0;
const BRAVE_SEARCH_DELAY_MS = 2000; // 2 seconds between calls as per Casey's requirement

/**
 * Log a search operation to JSONL file
 * @param {Object} logEntry - Log entry object
 */
function logSearch(logEntry) {
  try {
    const enrichedEntry = {
      timestamp: new Date().toISOString(),
      ...logEntry
    };

    const line = JSON.stringify(enrichedEntry) + '\n';
    fs.appendFileSync(SEARCH_LOG_PATH, line, 'utf-8');
  } catch (error) {
    console.error('[SearchLogger] Failed to write log:', error.message);
  }
}

/**
 * Wrap web_search tool calls with logging and rate limiting
 * @param {Function} webSearchTool - The original web_search tool function
 * @param {string} source - Source of the search (agent/cron/manual)
 * @returns {Function} Wrapped web_search function
 */
function createSearchLogger(webSearchTool, source = 'agent') {
  return async function wrappedWebSearch(query, options = {}) {
    const provider = 'Brave Search';
    const callId = `search_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;

    // Log search initiation
    logSearch({
      callId,
      action: 'initiated',
      provider,
      query,
      source,
      options: Object.keys(options).length > 0 ? options : undefined
    });

    // Enforce 2-second delay between consecutive Brave calls
    const timeSinceLastCall = Date.now() - lastBraveSearchTime;
    if (timeSinceLastCall < BRAVE_SEARCH_DELAY_MS) {
      const delayNeeded = BRAVE_SEARCH_DELAY_MS - timeSinceLastCall;
      console.log(`[SearchLogger] Rate limiting: waiting ${delayNeeded}ms before next Brave call`);
      await new Promise(resolve => setTimeout(resolve, delayNeeded));
    }

    lastBraveSearchTime = Date.now();

    try {
      // Execute the actual search
      const startTime = Date.now();
      const results = await webSearchTool(query, options);
      const duration = Date.now() - startTime;

      // Log successful completion
      logSearch({
        callId,
        action: 'completed',
        provider,
        query,
        source,
        durationMs: duration,
        resultCount: Array.isArray(results) ? results.length : 0
      });

      return results;
    } catch (error) {
      const duration = Date.now() - startTime;

      // Log error
      logSearch({
        callId,
        action: 'error',
        provider,
        query,
        source,
        durationMs: duration,
        errorMessage: error.message
      });

      throw error;
    }
  };
}

/**
 * Get search log statistics
 * @returns {Object} Statistics about searches today
 */
function getSearchStats() {
  if (!fs.existsSync(SEARCH_LOG_PATH)) {
    return { totalSearches: 0, byProvider: {}, bySource: {} };
  }

  try {
    const lines = fs.readFileSync(SEARCH_LOG_PATH, 'utf-8').trim().split('\n');
    const entries = lines
      .filter(line => line.trim())
      .map(line => JSON.parse(line));

    // Filter for today's entries
    const today = new Date().toISOString().split('T')[0];
    const todayEntries = entries.filter(e => e.timestamp?.startsWith(today));

    const stats = {
      totalSearches: todayEntries.filter(e => e.action === 'initiated').length,
      completedSearches: todayEntries.filter(e => e.action === 'completed').length,
      failedSearches: todayEntries.filter(e => e.action === 'error').length,
      byProvider: {},
      bySource: {},
      totalResults: 0,
      totalDuration: 0
    };

    todayEntries.forEach(entry => {
      if (entry.provider) {
        stats.byProvider[entry.provider] = (stats.byProvider[entry.provider] || 0) + 1;
      }
      if (entry.source) {
        stats.bySource[entry.source] = (stats.bySource[entry.source] || 0) + 1;
      }
      if (entry.resultCount) {
        stats.totalResults += entry.resultCount;
      }
      if (entry.durationMs) {
        stats.totalDuration += entry.durationMs;
      }
    });

    return stats;
  } catch (error) {
    console.error('[SearchLogger] Failed to parse log:', error.message);
    return { totalSearches: 0, error: error.message };
  }
}

module.exports = {
  createSearchLogger,
  logSearch,
  getSearchStats,
  SEARCH_LOG_PATH
};

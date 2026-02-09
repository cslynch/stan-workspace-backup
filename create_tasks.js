const {google} = require('googleapis');
const readline = require('readline');
const fs = require('fs');
const path = require('path');

const SCOPES = ['https://www.googleapis.com/auth/tasks'];
const TOKEN_PATH = path.join(__dirname, 'google-tasks-token.json');
const CREDENTIALS_PATH = path.join(__dirname, 'google-credentials.json');

const tasks_to_create = [
  {
    title: "Get Rosa's Telegram user ID and add her to group chat",
    notes: "Find Rosa's Telegram ID and add her to the main group chat"
  },
  {
    title: "Send Rosa Trello board invite link",
    notes: "Share the Trello board invite link with Rosa"
  },
  {
    title: "Set up Rosa with Google Workspace account",
    notes: "Create and configure Google Workspace account for Rosa"
  }
];

const tasklist_id = "NU5VRWVOZmNkT1FTYy1zVw";

async function loadSavedCredentials() {
  try {
    const content = fs.readFileSync(TOKEN_PATH);
    const credentials = JSON.parse(content);
    return google.auth.fromJSON(credentials);
  } catch (err) {
    return null;
  }
}

async function authorize() {
  // Check if we can load saved credentials
  let auth = await loadSavedCredentials();
  if (auth) {
    return auth;
  }

  // If no credentials file, we need to authenticate interactively
  if (!fs.existsSync(CREDENTIALS_PATH)) {
    console.error('No credentials.json found. Please set up Google OAuth.');
    console.error('Get credentials from: https://console.developers.google.com/');
    process.exit(1);
  }

  const credentials = JSON.parse(fs.readFileSync(CREDENTIALS_PATH));
  const {client_secret, client_id, redirect_uris} = credentials.installed;
  const oAuth2Client = new google.auth.OAuth2(client_id, client_secret, redirect_uris[0]);

  // Generate auth URL
  const authUrl = oAuth2Client.generateAuthUrl({
    access_type: 'offline',
    scope: SCOPES,
  });

  console.log('Authorize this app by visiting this url:', authUrl);
  
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  return new Promise((resolve) => {
    rl.question('Enter the code from that page here: ', async (code) => {
      rl.close();
      const {tokens} = await oAuth2Client.getToken(code);
      oAuth2Client.setCredentials(tokens);
      // Save the token to a file
      fs.writeFileSync(TOKEN_PATH, JSON.stringify(tokens));
      resolve(oAuth2Client);
    });
  });
}

async function createTasks(auth) {
  const tasks = google.tasks({version: 'v1', auth});

  console.log(`Creating ${tasks_to_create.length} tasks in list: ${tasklist_id}`);
  console.log('');

  let successCount = 0;
  let errorCount = 0;

  for (const task of tasks_to_create) {
    try {
      const result = await tasks.tasks.insert({
        tasklist: tasklist_id,
        requestBody: {
          title: task.title,
          notes: task.notes,
        },
      });

      console.log(`✓ Created: "${task.title}"`);
      console.log(`  ID: ${result.data.id}`);
      successCount++;
    } catch (error) {
      console.error(`✗ Failed to create: "${task.title}"`);
      console.error(`  Error: ${error.message}`);
      errorCount++;
    }
  }

  console.log('');
  console.log(`Summary: ${successCount} created, ${errorCount} failed`);
  return successCount;
}

async function main() {
  try {
    const auth = await authorize();
    await createTasks(auth);
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

main();

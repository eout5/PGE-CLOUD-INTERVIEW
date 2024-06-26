{
    "name": "@aws-sdk-notes-app/frontend",
    "version": "0.1.0",
    "private": true,
    "description": "Frontend for notes app created using modular AWS SDK for JavaScript",
    "dependencies": {
      "@aws-sdk/client-cognito-identity": "3.348.0",
      "@aws-sdk/client-polly": "3.348.0",
      "@aws-sdk/client-s3": "3.348.0",
      "@aws-sdk/client-transcribe-streaming": "3.348.0",
      "@aws-sdk/credential-provider-cognito-identity": "3.348.0",
      "@aws-sdk/polly-request-presigner": "3.348.0",
      "@aws-sdk/s3-request-presigner": "3.348.0",
      "@aws-sdk/util-create-request": "3.347.0",
      "@aws-sdk/util-format-url": "3.347.0",
      "@reach/router": "1.3.4",
      "p-event": "^6.0.1",
      "react": "18.2.0",
      "react-bootstrap": "1.4.0",
      "react-dom": "18.2.0"
    },
    "scripts": {
      "prepare:frontend": "cd .. && yarn prepare:frontend",
      "build": "tsc && vite build",
      "build:frontend": "cd .. && yarn build:frontend",
      "start": "vite --open",
      "start:frontend": "cd .. && yarn start:frontend",
      "cdk": "cd .. && yarn cdk"
    },
    "keywords": [
      "modular",
      "aws",
      "JavaScript",
      "TypeScript",
      "SDK",
      "v3"
    ],
    "author": "Kamat, Trivikram",
    "license": "MIT",
    "eslintConfig": {
      "extends": "react-app"
    },
    "browserslist": {
      "production": [
        ">0.2%",
        "not dead",
        "not op_mini all"
      ],
      "development": [
        "last 1 chrome version",
        "last 1 firefox version",
        "last 1 safari version"
      ]
    },
    "devDependencies": {
      "@types/node": "^18.11.18",
      "@types/reach__router": "1.3.6",
      "@types/react": "^18.0.15",
      "@types/react-dom": "^18.0.6",
      "@vitejs/plugin-react-refresh": "1.3.6",
      "react-bootstrap-icons": "1.3.0",
      "typescript": "~4.9.4",
      "vite": "5.2.7"
    },
    "type": "module"
  }
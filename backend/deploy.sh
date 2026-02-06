# Deploy to Google Cloud Functions
# Make sure you have the gcloud CLI installed and authenticated

PROJECT_ID=$(gcloud config get-value project)
REGION="us-central1"
FUNCTION_NAME="submit-lead"

echo "Deploying function $FUNCTION_NAME to project $PROJECT_ID in $REGION..."

gcloud functions deploy $FUNCTION_NAME \
    --gen2 \
    --runtime=python311 \
    --region=$REGION \
    --source=. \
    --entry-point=submit_lead \
    --trigger-http \
    --allow-unauthenticated

echo "Deployment complete. Use the URL above in your HTML forms."

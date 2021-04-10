resource "aws_lambda_function" "lambda" {
  function_name = "${local.project_name}-api"
  role          = aws_iam_role.lambda.name

  runtime          = "python3.8"
  filename         = "../build.zip"
  source_code_hash = filebase64sha256("../build.zip")
  handler          = "geopatterns_demo.api.app"

  timeout     = 900
  memory_size = 512
  reserved_concurrent_executions = 5

  description = "This Lambda function handles the API requests - both to create geopatterns images and to list images which were already created."
}

resource "aws_lambda_function" "lambda" {
  function_name = "${local.project_name}-api"
  role          = aws_iam_role.lambda.arn

  runtime          = "python3.8"
  filename         = "${path.module}/.terraform/build.zip"
  source_code_hash = data.archive_file.lambda_code.output_base64sha256
  handler          = "geopatterns_demo.api.lambda_handler"

  timeout     = 900
  memory_size = 512
  reserved_concurrent_executions = 5

  description = "This Lambda function handles the API requests - both to create geopatterns images and to list images which were already created."
}

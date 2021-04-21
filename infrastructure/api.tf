resource "aws_apigatewayv2_api" "api" {
  # HTTP API we will use to call our function and get its execution results
  name          = "${local.project_name}-api"
  protocol_type = "HTTP"
  target        = aws_lambda_function.lambda.arn

  cors_configuration {
    allow_origins = [
      "https://anatoly-scherbakov.github.io",
      "http://localhost:9010"
    ]
    allow_methods = ["GET"]
  }
}


resource "aws_lambda_permission" "allow-api-gateway-to-call-lambda" {
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda.arn
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.api.execution_arn}/*/*"
}

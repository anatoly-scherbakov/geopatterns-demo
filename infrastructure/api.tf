resource "aws_api_gateway_rest_api" "api" {
  name = "${local.project_name}-api"
}

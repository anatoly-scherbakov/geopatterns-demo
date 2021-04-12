locals {
  layer_filename = "../layer/geopatterns_demo_lambda_layer.zip"
}

resource aws_lambda_layer_version libraries {
  layer_name = "${local.project_name}-binaries"
  filename = local.layer_filename
  source_code_hash = filebase64sha256(local.layer_filename)
  compatible_runtimes = ["python3.8"]
}

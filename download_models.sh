#!/bin/bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
./aws/install
aws s3 cp s3://xvector-hack/mobileclip_s0.pt ./models/mobileclip_s0.pt --no-sign-request
aws s3 cp s3://xvector-hack/bge.quant.onnx ./models/bge.quant.onnx --no-sign-request

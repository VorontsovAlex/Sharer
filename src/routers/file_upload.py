# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...)):
#     try:
#         contents = await file.read()
#         # You can process the contents of the file here
#         # For demonstration, let's just return a JSON response with the file details
#         return JSONResponse(content={"filename": file.filename, "content_type": file.content_type})
#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)
#
#
#
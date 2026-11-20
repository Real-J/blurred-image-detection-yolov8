

# from PIL import Image
# import os

# def resize_images(input_dir, output_dir, target_size, output_file_name):
#     # Create the output directory if it doesn't exist
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     # Iterate over the files in the input directory
#     for filename in os.listdir(input_dir):
#         if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust the file extensions as needed
#             # Open the image file
#             image_path = os.path.join(input_dir, filename)
#             image = Image.open(image_path)

#             # Resize the image
#             resized_image = image.resize((target_size, target_size))

#             # Set the output file name
#             output_filename = output_file_name + os.path.splitext(filename)[0] + ".jpg"  # Adjust the file extension as needed

#             # Save the resized image to the output directory
#             output_path = os.path.join(output_dir, output_filename)
#             resized_image.save(output_path)

#             # Close the image file
#             image.close()

# # Set the input directory, output directory, target size, and output file name
# input_directory = "/Users/mathew/Desktop/O250/val"  # Replace with the path to your input directory
# output_directory = "/Users/mathew/Desktop/250res"  # Replace with the path to your output directory
# target_size = 256
# output_file_name = "resized_"  # Specify your desired output file name prefix

# # Resize the images
# resize_images(input_directory, output_directory, target_size, output_file_name)






from PIL import Image
import os

def convert_to_grayscale(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over the files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust the file extensions as needed
            # Open the image file
            image_path = os.path.join(input_dir, filename)
            image = Image.open(image_path)

            # Convert the image to grayscale
            grayscale_image = image.convert("L")

            # Save the grayscale image to the output directory
            output_path = os.path.join(output_dir, filename)
            grayscale_image.save(output_path)

            # Close the image file
            image.close()

# Set the input directory, output directory
input_directory = "/Users/mathew/Desktop/25res"  # Replace with the path to your input directory
output_directory = "Users/mathew/Desktop/25res/bw"  # Replace with the path to your output directory

# Convert the images to grayscale
convert_to_grayscale(input_directory, output_directory)

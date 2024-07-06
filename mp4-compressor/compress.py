import subprocess

input_file = "input.mp4"  # path to your input file
output_file = "output.mp4"  # path to your output file

# command to compress the video
command = f"ffmpeg -i {input_file} -vcodec libx264 -crf 28 {output_file}"

# run the command
subprocess.call(command, shell=True)

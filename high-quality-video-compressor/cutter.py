from moviepy.editor import VideoFileClip

def compress_video(input_file, output_file, bitrate='1000k'):
    video = VideoFileClip(input_file)
    
    # Compress the video with the specified bitrate
    compressed_video = video.resize(width=video.w // 2, height=video.h // 2).\
                       write_videofile(output_file, bitrate=bitrate)
    
    video.close()

# Example usage:
input_file = "your_video.mp4"
output_file = "compressed_video.mp4"
bitrate = '500k'  # Adjust the bitrate as needed

compress_video(input_file, output_file, bitrate)

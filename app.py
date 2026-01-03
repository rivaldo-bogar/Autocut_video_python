import subprocess
import os


class VideoAutoCutter:
    def __init__(self, input_video, output_dir, segment_duration=20):
        """
        Constructor / inisialisasi class

        input_video       : lokasi file video asli
        output_dir        : folder penyimpanan hasil potongan
        segment_duration  : durasi potongan (detik)
        """

        self.input_video = input_video
        self.output_dir = output_dir
        self.segment_duration = segment_duration

        # output directory, /bogar/--> C: 'liat path'
        os.makedirs(self.output_dir, exist_ok=True)

    def cut_video(self):
        """
        Fungsi utama untuk memotong video
        """

    def cut_video(self):
            command = [
        "ffmpeg",
        "-i", self.input_video,
        "-map", "0",
        "-segment_time", str(self.segment_duration),
        "-f", "segment",
        "-reset_timestamps", "1",
        "-c:v", "libx264",     # encode ulang video
        "-preset", "fast",
        "-crf", "18",          # kualitas tinggi (hampir lossless)
        "-c:a", "aac",         # encode audio
        f"{self.output_dir}/part_%03d.mp4"
            ]

                # Jalankan perintah ffmpeg
            subprocess.run(command, check=True)

    print("✅ Video berhasil dipotong tanpa penurunan kualitas")


# =======================
# CARA MENJALANKAN PROGRAM
# =======================

if __name__ == "__main__":
    cutter = VideoAutoCutter(
        input_video="input/video.mp4",
        output_dir="output",
        segment_duration=30
    )

    cutter.cut_video()

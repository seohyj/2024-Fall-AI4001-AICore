import cv2
import os

class FrameCapture:
    def __init__(self, video_path, interval=0.1):
        self.video_path = video_path
        self.interval = interval
        self.video_name = os.path.basename(video_path)  # 비디오 파일명 (예: "2.mp4")
        self.video_number = os.path.splitext(self.video_name)[0]  # 확장자 제거 (예: "2")
        self.output_dir = f"frames_{self.video_number}"  # 기본 출력 폴더 이름
        self.cap = None
        self.fps = 0
        self.total_frames = 0

    def setup_output_directory(self):
        """출력 디렉토리를 생성합니다."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            print(f"Directory '{self.output_dir}' created.")
        else:
            print(f"Directory '{self.output_dir}' already exists.")

    def open_video(self):
        """비디오 파일을 열고 FPS와 총 프레임 수를 가져옵니다."""
        self.cap = cv2.VideoCapture(self.video_path)
        if not self.cap.isOpened():
            raise FileNotFoundError(f"Error: Unable to open video file {self.video_path}")
        
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        if self.fps <= 0:
            raise ValueError("Error: Unable to fetch FPS from the video file.")
        print(f"FPS: {self.fps}")
        
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f"Total frames: {self.total_frames}")

    def capture_frames(self):
        """비디오에서 프레임을 캡처하고 저장합니다."""
        self.setup_output_directory()
        self.open_video()

        frame_interval = int(self.fps * self.interval)
        frame_count = 0
        saved_frame_count = 0

        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            if frame_count % frame_interval == 0:
                frame_name = f"{self.output_dir}/frame_{saved_frame_count:04d}.jpg"
                cv2.imwrite(frame_name, frame)
                print(f"Saved: {frame_name}")
                saved_frame_count += 1

            frame_count += 1

        self.cap.release()
        print(f"Total images saved: {saved_frame_count} to {self.output_dir}")

# 사용 방법
if __name__ == "__main__":
    video_path = "3.mp4"  # 분석할 비디오 파일 경로
    frame_capture = FrameCapture(video_path, interval=0.1)
    frame_capture.capture_frames()

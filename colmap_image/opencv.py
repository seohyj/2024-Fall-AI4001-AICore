import cv2
import os

def capture_frames(video_path, output_dir, interval=1):
    # 비디오 파일 열기
    cap = cv2.VideoCapture(video_path)
    
    # 저장할 디렉토리 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 비디오의 FPS와 총 프레임 수 가져오기
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # 1초 간격으로 프레임을 캡처
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # 1초 단위 프레임 캡처
        if frame_count % (fps * interval) == 0:
            # 파일명 생성 및 저장
            frame_name = f"{output_dir}/frame_{frame_count // fps}.jpg"
            cv2.imwrite(frame_name, frame)
        
        frame_count += 1
    
    cap.release()
    print(f"Images saved to {output_dir}")

# 사용 예제
video_path = "./1.mp4"  # 분석할 비디오 파일 경로
output_dir = "./captured_frames"  # 캡처한 이미지 저장 디렉토리
capture_frames(video_path, output_dir)

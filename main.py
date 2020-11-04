import filters
import cv2

def main():
    imageWithoutNoise = cv2.imread("images/manul.jpg")
    imageWithNoise = task_1_noise(imageWithoutNoise)
    task_2_averaging_filter(imageWithNoise)
    task_2_median_filter(imageWithNoise)
    task_3_cv2(imageWithNoise)

def task_1_noise(image):
    task_1_noise_result = filters.add_gaussian_noise(image=image, mu=20, sigma=15)
    cv2.imwrite("result/task1/manulNoise.png", task_1_noise_result)
    return task_1_noise_result

def task_2_median_filter(image):
    task_2_med_result = filters.median_filter(image = image, kernel_radius=1)
    cv2.imwrite('result/task2/median_filter.png', task_2_med_result)

def task_2_averaging_filter(image):
    task_2_av_result = filters.averaging_filter(image, radius = 1)
    cv2.imwrite('result/task2/average_filter.png', task_2_av_result)

def task_3_cv2(image):
	med_cv2 = cv2.medianBlur(image, 3)
	average_cv2 = cv2.blur(image, (3, 3))

	cv2.imwrite('result/task3/noise_src.png', image)
	cv2.imwrite('result/task3/median_cv2.png', med_cv2)
	cv2.imwrite('result/task3/average_cv2.png', average_cv2)

if __name__ == '__main__':
	main()
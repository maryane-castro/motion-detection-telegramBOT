import cv2


# Inicializa o objeto de captura de vídeo
cap = cv2.VideoCapture(0)  # 0 indica a câmera padrão do sistema

# Inicializa o objeto de detector de movimento
fgbg = cv2.createBackgroundSubtractorMOG2()

# Define o limite mínimo da área do contorno
min_contour_area = 45000


count = 0
while True:
    # Lê o próximo quadro do fluxo de vídeo
    ret, frame = cap.read()

    # Aplica o detector de movimento no quadro atual
    fgmask = fgbg.apply(frame)

    # Encontra os contornos dos objetos em movimento
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Verifica se há algum contorno detectado (movimento)
    for contour in contours:
        if cv2.contourArea(contour) > min_contour_area:
            print("Alguém passou!", count)
            count += 1

    # Mostra o quadro com o resultado da detecção de movimento
    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fgmask)

    # Verifica se o usuário pressionou a tecla 'q' para sair
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Libera os recursos
cap.release()
cv2.destroyAllWindows()

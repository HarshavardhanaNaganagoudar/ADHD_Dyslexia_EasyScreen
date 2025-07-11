import pygame
import random
import time
import json

# Init
pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Game - ADHD Test")

FONT = pygame.font.SysFont("Arial", 32)
BIG_FONT = pygame.font.SysFont("Arial", 48)

# Colors
COLORS = {
    "red": (255, 80, 80),
    "green": (80, 255, 80),
    "blue": (80, 80, 255),
    "yellow": (255, 255, 80)
}
COLOR_KEYS = list(COLORS.keys())

# Layout
GRID_POS = [(200, 200), (400, 200), (200, 400), (400, 400)]
SQUARE_SIZE = 150

# Results
results = {
    "rounds": 0,
    "mistakes": 0,
    "click_times_ms": [],
    "max_sequence_recalled": 0
}

def draw_grid():
    for i, color in enumerate(COLOR_KEYS):
        x, y = GRID_POS[i]
        pygame.draw.rect(WIN, COLORS[color], (x, y, SQUARE_SIZE, SQUARE_SIZE))
    pygame.display.update()

def flash_sequence(seq):
    for color in seq:
        i = COLOR_KEYS.index(color)
        x, y = GRID_POS[i]
        pygame.draw.rect(WIN, COLORS[color], (x, y, SQUARE_SIZE, SQUARE_SIZE))
        pygame.display.update()
        time.sleep(0.5)
        pygame.draw.rect(WIN, (30, 30, 30), (x, y, SQUARE_SIZE, SQUARE_SIZE))
        pygame.display.update()
        time.sleep(0.2)
    draw_grid()

def get_color_clicked(pos):
    for i, (x, y) in enumerate(GRID_POS):
        if x <= pos[0] <= x + SQUARE_SIZE and y <= pos[1] <= y + SQUARE_SIZE:
            return COLOR_KEYS[i]
    return None

def show_text(msg, y_offset=0):
    WIN.fill((255, 255, 255))
    text = BIG_FONT.render(msg, True, (0, 0, 0))
    WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + y_offset))
    pygame.display.update()

def run_memory_game():
    sequence = []
    level = 1
    running = True

    show_text("Click to Start")
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

    while running:
        sequence.append(random.choice(COLOR_KEYS))
        results["rounds"] += 1
        show_text(f"Round {level}")
        time.sleep(1)

        WIN.fill((30, 30, 30))
        draw_grid()
        flash_sequence(sequence)

        user_sequence = []
        index = 0
        start_time = time.time()
        while index < len(sequence):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_color = get_color_clicked(pygame.mouse.get_pos())
                    if not clicked_color:
                        continue

                    rt = int((time.time() - start_time) * 1000)
                    results["click_times_ms"].append(rt)

                    if clicked_color == sequence[index]:
                        user_sequence.append(clicked_color)
                        index += 1
                        start_time = time.time()
                    else:
                        results["mistakes"] += 1
                        show_text("❌ Wrong! Game Over")
                        running = False
                        break
            else:
                continue
            break

        if running:
            results["max_sequence_recalled"] = len(sequence)
            level += 1
            start_time = time.time()

    pygame.quit()
    with open("memory_game_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("📝 Results saved to memory_game_results.json")
    print(json.dumps(results, indent=2))
    return True

if __name__ == "__main__":
    run_memory_game()

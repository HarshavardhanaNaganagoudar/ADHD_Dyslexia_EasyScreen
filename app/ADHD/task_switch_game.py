import pygame
import random
import time
import json

# Game setup
pygame.init()
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ADHD Task Switching Test")

FONT = pygame.font.SysFont(None, 36)
BIG_FONT = pygame.font.SysFont(None, 48)

COLORS = {"red": (255, 0, 0), "blue": (0, 0, 255), "green": (0, 255, 0)}
TASKS = ["Tap only RED", "Now tap only GREEN", "Now tap only BLUE"]
TASK_KEYS = ["red", "green", "blue"]

# Track performance
results = {
    "reaction_times_ms": [],
    "errors": 0,
    "task_switch_accuracy": []
}

def draw_start_screen():
    WIN.fill((255, 255, 255))
    title = BIG_FONT.render("ADHD Task Switching Test", True, (0, 0, 0))
    start_msg = FONT.render("Click anywhere to start", True, (0, 0, 0))
    WIN.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    WIN.blit(start_msg, (WIDTH // 2 - start_msg.get_width() // 2, HEIGHT // 2))
    pygame.display.update()

def wait_for_click():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

def get_random_boxes():
    positions = [(100, 150), (250, 150), (400, 150)]
    random.shuffle(positions)
    keys = list(COLORS.keys())
    return {keys[i]: pygame.Rect(positions[i][0], positions[i][1], 100, 100) for i in range(3)}

def draw_screen(active_task, boxes):
    WIN.fill((255, 255, 255))
    
    # Draw instruction
    instruction = FONT.render(TASKS[active_task], True, (0, 0, 0))
    WIN.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, 50))

    # Draw boxes
    for color, rect in boxes.items():
        pygame.draw.rect(WIN, COLORS[color], rect)

    pygame.display.update()

def get_clicked_color(pos, boxes):
    for color, rect in boxes.items():
        if rect.collidepoint(pos):
            return color
    return None

def run_task_switch_game(rounds=6):
    draw_start_screen()
    wait_for_click()

    running = True
    task_index = 0

    while running and task_index < rounds:
        boxes = get_random_boxes()
        draw_screen(task_index % len(TASKS), boxes)
        pygame.event.clear()

        start = time.time()
        clicked = False

        while not clicked:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_color = get_clicked_color(pygame.mouse.get_pos(), boxes)
                    if clicked_color:
                        reaction_time = int((time.time() - start) * 1000)
                        correct_color = TASK_KEYS[task_index % len(TASK_KEYS)]

                        if clicked_color == correct_color:
                            results["reaction_times_ms"].append(reaction_time)
                            results["task_switch_accuracy"].append(1)
                        else:
                            results["errors"] += 1
                            results["task_switch_accuracy"].append(0)

                        task_index += 1
                        clicked = True

        # Optional delay between tasks
        time.sleep(0.5)

    pygame.quit()

    with open("task_switch_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("✅ Task Switching Test Complete")
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    run_task_switch_game()

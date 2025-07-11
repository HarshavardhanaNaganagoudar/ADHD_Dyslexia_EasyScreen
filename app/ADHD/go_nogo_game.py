import pygame
import random
import time
import json

# Init
pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Go / No-Go ADHD Test")

FONT = pygame.font.SysFont("Arial", 32)

# Colors
BLUE = (0, 122, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

CIRCLE_RADIUS = 60
CIRCLE_POS = (WIDTH // 2, HEIGHT // 2)

# Settings
TOTAL_TRIALS = 20
STIMULUS_DURATION = 1.2  # seconds to display
INTERVAL = 1.8           # seconds between stimuli

# Results logging
results = {
    "hits": 0,
    "misses": 0,
    "false_alarms": 0,
    "reaction_times_ms": []
}

def draw_text(text, y):
    label = FONT.render(text, True, (0, 0, 0))
    WIN.blit(label, (WIDTH // 2 - label.get_width() // 2, y))

def run_game():
    trial = 0
    clock = pygame.time.Clock()
    running = True

    WIN.fill(WHITE)
    draw_text("Click only on BLUE circles. Press SPACE to start.", 250)
    pygame.display.update()

    # Wait for space
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                break
        else:
            continue
        break

    time.sleep(1)

    while running and trial < TOTAL_TRIALS:
        WIN.fill(WHITE)
        draw_text(f"Trial {trial+1}/{TOTAL_TRIALS}", 20)

        # Choose circle color
        stimulus_type = random.choice(["blue", "red"])
        color = BLUE if stimulus_type == "blue" else RED
        pygame.draw.circle(WIN, color, CIRCLE_POS, CIRCLE_RADIUS)
        pygame.display.update()

        clicked = False
        stimulus_start = time.time()

        # Wait for response
        while time.time() - stimulus_start < STIMULUS_DURATION:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    rt = (time.time() - stimulus_start) * 1000  # in ms
                    clicked = True
                    if stimulus_type == "blue":
                        results["hits"] += 1
                        results["reaction_times_ms"].append(rt)
                    else:
                        results["false_alarms"] += 1
                    break
            if not running:
                break
            clock.tick(60)

        # No click on blue = miss
        if stimulus_type == "blue" and not clicked:
            results["misses"] += 1

        pygame.display.flip()
        time.sleep(INTERVAL)
        trial += 1

    pygame.quit()

    # Save results
    with open("go_nogo_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("📝 Results saved to go_nogo_results.json")
    print(json.dumps(results, indent=2))
    return True

if __name__ == "__main__":
    run_game()
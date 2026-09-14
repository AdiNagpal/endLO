
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Beat Grid")

clock = pygame.time.Clock()

keys = [pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k]
key_names = ["D", "F", "J", "K"]

score = 0
combo = 0
speed = 5
hit_y = 600

font = pygame.font.Font(None, 36)

# Create a new note
def new_note(i):
    x = 75 + i * 150
    y = random.randint(-500, -50)
    return pygame.Rect(x, y, 50, 30)

# Create notes for each lane
notes = []

for i in range(4):
    notes.append(new_note(i))

running = True

while running:

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            for i, key in enumerate(keys):

                if event.key == key:

                    if abs(notes[i].y - hit_y) < 35:
                        score += 100
                        combo += 1
                        notes[i] = new_note(i)

                    else:
                        combo = 0

    # Move the notes
    for i, note in enumerate(notes):

        note.y += speed

        # Reset notes that go below the screen
        if note.y > 700:
            notes[i] = new_note(i)
            combo = 0

    # Background
    screen.fill((20, 20, 30))

    # Draw lane lines
    for i in range(4):
        x = 50 + i * 150

        pygame.draw.line(
            screen,
            (70, 70, 90),
            (x, 0),
            (x, 700),
            2
        )

    # Draw hit line
    pygame.draw.line(
        screen,
        (255, 255, 255),
        (0, hit_y),
        (600, hit_y),
        3
    )

    # Draw notes
    for note in notes:

        pygame.draw.rect(
            screen,
            (0, 200, 255),
            note
        )

    # Display score
    score_text = font.render(
        "Score: " + str(score),
        True,
        (255, 255, 255)
    )

    # Display combo
    combo_text = font.render(
        "Combo: " + str(combo),
        True,
        (255, 255, 255)
    )

    screen.blit(score_text, (20, 20))
    screen.blit(combo_text, (20, 60))

    # Display the keys at the bottom
    for i in range(4):

        key_text = font.render(
            key_names[i],
            True,
            (255, 255, 255)
        )

        screen.blit(
            key_text,
            (95 + i * 150, 650)
        )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
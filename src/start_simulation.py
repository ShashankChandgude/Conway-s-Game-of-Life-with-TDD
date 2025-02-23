# pragma: no cover
import pygame
from game_of_life import next_generation

# Constants
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 30
TOP_MARGIN = 40
SCREEN_PADDING = 120
EXTRA_WIDTH = 200

# Colors
BG_COLOR = (245, 245, 245)
LIVE_COLOR = (34, 139, 34)
DEAD_COLOR = (255, 255, 255)
GRID_LINE_COLOR = (200, 200, 200)
BUTTON_COLOR = (70, 130, 180)
HOVER_BUTTON_COLOR = (100, 160, 210)
ACTIVE_BUTTON_COLOR = (0, 150, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)
TITLE_COLOR = (50, 50, 50)
OUTLINE_COLOR = (100, 100, 100)

pygame.init()
FONT = pygame.font.SysFont("Verdana", 24)
TITLE_FONT = pygame.font.SysFont("Verdana", 48)

def draw_title(screen):
   
    title_surf = TITLE_FONT.render("Conway's Game of Life", True, TITLE_COLOR)
    title_rect = title_surf.get_rect(center=(screen.get_width() // 2, TOP_MARGIN // 2))
    screen.blit(title_surf, title_rect)

def draw_grid(screen, live_cells):
    
    grid_w = GRID_WIDTH * CELL_SIZE
    offset_x = (screen.get_width() - grid_w) // 2
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            sx = offset_x + x * CELL_SIZE
            sy = TOP_MARGIN + y * CELL_SIZE
            rect = pygame.Rect(sx, sy, CELL_SIZE, CELL_SIZE)
            color = LIVE_COLOR if (x, y) in live_cells else DEAD_COLOR
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRID_LINE_COLOR, rect, 1)
    grid_rect = pygame.Rect(offset_x, TOP_MARGIN, grid_w, GRID_HEIGHT * CELL_SIZE)
    pygame.draw.rect(screen, OUTLINE_COLOR, grid_rect, 3)

def compute_button_color(key, btn, infinite_generation, mouse_pos):
    
    if btn["rect"].collidepoint(mouse_pos) and not (key == "start" and infinite_generation):
        return HOVER_BUTTON_COLOR
    return ACTIVE_BUTTON_COLOR if key == "start" and infinite_generation else BUTTON_COLOR

def draw_buttons(screen, buttons, infinite_generation):
   
    mouse_pos = pygame.mouse.get_pos()
    for key, btn in buttons.items():
        text = "Stop" if key == "start" and infinite_generation else btn["text"]
        color = compute_button_color(key, btn, infinite_generation, mouse_pos)
        pygame.draw.rect(screen, color, btn["rect"], border_radius=8)
        pygame.draw.rect(screen, (0, 0, 0), btn["rect"], 2, border_radius=8)
        text_surf = FONT.render(text, True, BUTTON_TEXT_COLOR)
        screen.blit(text_surf, text_surf.get_rect(center=btn["rect"].center))

def display(screen, live_cells, buttons, infinite_generation):
    
    screen.fill(BG_COLOR)
    draw_title(screen)
    draw_grid(screen, live_cells)
    draw_buttons(screen, buttons, infinite_generation)
    pygame.display.flip()

def update_buttons(screen_width, screen_height):
   
    bw, bh = 140, 40
    num_buttons = 3
    spacing = (screen_width - num_buttons * bw) // (num_buttons + 1)
    y = screen_height - 60
    return {
        "next_gen": {"text": "Next Gen", "rect": pygame.Rect(spacing, y, bw, bh)},
        "start": {"text": "Start", "rect": pygame.Rect(2 * spacing + bw, y, bw, bh)},
        "clear": {"text": "Clear", "rect": pygame.Rect(3 * spacing + 2 * bw, y, bw, bh)}
    }

def handle_grid_click(mx, my, live_cells, screen_width):

    grid_px = GRID_WIDTH * CELL_SIZE
    offset_x = (screen_width - grid_px) // 2
    if offset_x <= mx < offset_x + grid_px and TOP_MARGIN <= my < TOP_MARGIN + GRID_HEIGHT * CELL_SIZE:
        x = (mx - offset_x) // CELL_SIZE
        y = (my - TOP_MARGIN) // CELL_SIZE
        new_live = set(live_cells)
        cell = (x, y)
        if cell in new_live:
            new_live.remove(cell)
        else:
            new_live.add(cell)
        return new_live
    return live_cells

def handle_mouse_event(event, live_cells, infinite_generation, buttons, screen_width):
   
    mx, my = event.pos
    if buttons["next_gen"]["rect"].collidepoint(mx, my):
        return next_generation(live_cells), infinite_generation
    if buttons["start"]["rect"].collidepoint(mx, my):
        return live_cells, not infinite_generation
    if buttons["clear"]["rect"].collidepoint(mx, my):
        return set(), False
    return handle_grid_click(mx, my, live_cells, screen_width), infinite_generation

def handle_events(screen, buttons, live_cells, infinite):
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, live_cells, infinite, buttons, screen
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            sw, sh = event.size
            buttons = update_buttons(sw, sh)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            live_cells, infinite = handle_mouse_event(event, live_cells, infinite, buttons, screen.get_width())
    return True, live_cells, infinite, buttons, screen

def simulation_loop(screen, buttons):
    
    live_cells = set()
    infinite = False
    clock = pygame.time.Clock()
    running = True
    while running:
        running, live_cells, infinite, buttons, screen = handle_events(screen, buttons, live_cells, infinite)
        if infinite:
            live_cells = next_generation(live_cells)
            if not live_cells:
                infinite = False
            pygame.time.delay(200)
        display(screen, live_cells, buttons, infinite)
        clock.tick(60)
    return screen

def run_simulation():
   
    init_width = GRID_WIDTH * CELL_SIZE + EXTRA_WIDTH
    init_height = TOP_MARGIN + GRID_HEIGHT * CELL_SIZE + SCREEN_PADDING
    screen = pygame.display.set_mode((init_width, init_height), pygame.RESIZABLE)
    pygame.display.set_caption("Game of Life")
    buttons = update_buttons(init_width, init_height)
    simulation_loop(screen, buttons)
    pygame.quit()

if __name__ == "__main__":
    run_simulation()

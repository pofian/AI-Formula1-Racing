import pygame
import math
import numpy as np

class Car:

    def __init__(self, sprite, size, position):
        self.must_draw = False

        self.sprite = sprite
        self.position = position
        self.set_angle(0)
        self.set_size(size)

        self.speed = 0
        self.distance = 0
        self.time = 0
        self.alive = True

    def start_drawing(self):
        if self.must_draw:
            return
        self.must_draw = True
        self.sprite_resized = pygame.transform.scale(self.sprite, self.size)
        self.rotate_sprite()

    def stop_drawing(self):
        self.must_draw = False

    def set_size(self, size):
        self.size = size
        self.sprite_resized = pygame.transform.scale(self.sprite, self.size)
        if self.must_draw:
            self.rotate_sprite()

    def set_angle(self, angle):
        self.angle = angle
        angle_rads = math.radians(angle)
        self.direction = [math.cos(angle_rads), -math.sin(angle_rads)]
        self.rotate_sprite()

    def rotate_sprite(self):
        if self.must_draw:
            self.rotated_sprite = pygame.transform.rotate(self.sprite_resized, self.angle)

    def set_position(self, position):
        self.position = position

    def is_alive(self):
        return self.alive

    def draw(self, screen):
        if self.must_draw:
            screen.blit(self.rotated_sprite, self.position)

    def check_collision(self, map):
        pass

    def update(self):
        pass

    def update_position(self, choice):
        match (choice) :
            case 0:
                pass
        pass

    def update_position_from_keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.set_position(np.add(self.position,
                                np.multiply(self.size[0] / 50, self.direction)))
        if keys[pygame.K_a]:
            self.position[0] -= self.size[0] / 200
        if keys[pygame.K_d]:
            self.position[0] += self.size[0] / 200
        if keys[pygame.K_s]:
            self.position[1] += self.size[1] / 200

        if keys[pygame.K_z]:
            self.set_size([size / 1.01 for size in self.size])
        if keys[pygame.K_x]:
            self.set_size([size * 1.01 for size in self.size])

        if keys[pygame.K_q]:
            self.set_angle(self.angle + 0.5)
        if keys[pygame.K_e]:
            self.set_angle(self.angle - 0.5)

    def get_data(self):
        pass

    def get_reward(self):
        return 0

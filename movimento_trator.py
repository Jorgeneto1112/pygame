while state != DONE:
    clock.tick(FPS)
  
    for event in pygame.event.get():
            
        if event.type == pygame.QUIT:
            state = DONE
            
        if state == PLAYING:
                
            if event.type == pygame.KEYDOWN:
                   
                keys_down[event.key] = True
                if event.key == pygame.K_LEFT:
                    player.speedx -= 8
                if event.key == pygame.K_RIGHT:
                    player.speedx += 8
                if event.key == pygame.K_UP:
                    player.rect.y -= 15
                if event.key == pygame.K_DOWN:
                    player.rect.y += 15
               
            if event.type == pygame.KEYUP:
                   
                if event.key in keys_down and keys_down[event.key]:
                    if event.key == pygame.K_LEFT:
                        player.speedx += 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx -= 8
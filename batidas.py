if condicao == PLAYING:
    pontos += 1


    

    hits = pygame.sprite.spritecollide(jogador, all_cavalos, True, pygame.sprite.collide_mask)
    hits1 = pygame.sprite.spritecollide(jogador, all_galinhas, True, pygame.sprite.collide_mask)
    if len(hits) > 0 or len(hits1) > 0:

        assets['som animal'].play()
        jogador.kill()
        vidas -= 1
        morte = Morte(jogador.rect.center, assets)
        all_sprites.add(morte)
        condicao = MORRENDO
        keys_down = {}
        morte_tick = pygame.time.get_ticks()
        morte_duration = morte.frame_ticks * len(morte.caveira_anim) + 400
elif condicao == MORRENDO:
    agora = pygame.time.get_ticks()
    if agora - morte_tick > morte_duration:
        if vidas == 0:
            condicao = DONE
        else:
            condicao = PLAYING
            jogador = Trator(groups, assets)
            all_sprites.add(jogador)
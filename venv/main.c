#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>
#include <stdbool.h>

#define WINDOW_WIDTH 480
#define WINDOW_HEIGHT 320

void render_text(SDL_Renderer *renderer, TTF_Font *font, const char *text, int x, int y, SDL_Color color) {
    SDL_Surface *surface = TTF_RenderText_Blended(font, text, color);
    SDL_Texture *texture = SDL_CreateTextureFromSurface(renderer, surface);
    SDL_Rect dest = {x, y, surface->w, surface->h};
    SDL_RenderCopy(renderer, texture, NULL, &dest);
    SDL_FreeSurface(surface);
    SDL_DestroyTexture(texture);
}

void render_icon(SDL_Renderer *renderer, SDL_Texture *texture, int x, int y) {
    SDL_Rect dest = {x, y, 50, 50}; // Taille de l'icône
    SDL_RenderCopy(renderer, texture, NULL, &dest);
}

bool is_mouse_over(int mouse_x, int mouse_y, SDL_Rect rect) {
    return mouse_x >= rect.x && mouse_x <= rect.x + rect.w &&
           mouse_y >= rect.y && mouse_y <= rect.y + rect.h;
}

int main(int argc, char *argv[]) {
    
    SDL_Init(SDL_INIT_VIDEO);
    TTF_Init();

    SDL_Window *window = SDL_CreateWindow("Vérification des capteurs", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH, WINDOW_HEIGHT, 0);
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    if(argc == 2)
    {
        if(argv[1][1] = 'F')
        {
            SDL_SetWindowFullscreen(window, SDL_WINDOW_FULLSCREEN);
        }   
    }
    

    TTF_Font *font = TTF_OpenFont("arial.ttf", 24);
    if (!font) {
        printf("Erreur chargement police : %s\n", TTF_GetError());
        return -1;
    }

    SDL_Color white = {255, 255, 255, 255};
    SDL_Color green = {0, 255, 0, 255};
    SDL_Color red = {255, 0, 0, 255};
    SDL_Color yellow = {255, 255, 0, 255};
    SDL_Color blue = {0, 0, 255, 255};

    bool running = true;
    SDL_Event event;
    bool button_clicked = false;

    SDL_Rect button = {180, 230, 140, 50}; // Bouton "Continuer"

    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = false;
            } else if (event.type == SDL_MOUSEBUTTONDOWN && event.button.button == SDL_BUTTON_LEFT) {
                int mouse_x = event.button.x;
                int mouse_y = event.button.y;

                // Vérifie si la souris est sur le bouton
                if (is_mouse_over(mouse_x, mouse_y, button)) {
                    button_clicked = true; // Marque le bouton comme cliqué
                    printf("Bouton 'Continuer' clique !\n");
                }
            }
        }

        SDL_SetRenderDrawColor(renderer, blue.r, blue.g, blue.b, blue.a); 
        SDL_RenderClear(renderer);

        // Texte principal
        render_text(renderer, font, "Verification des capteurs :", 120, 20, white);

        // Statuts
        render_text(renderer, font, "GPS", 60, 100, white);
        render_text(renderer, font, "OK", 70, 140, green);

        render_text(renderer, font, "Vitesse", 140, 100, white);
        render_text(renderer, font, "OK", 170, 140, green);

        render_text(renderer, font, "SIM", 260, 100, white);
        render_text(renderer, font, "KO", 270, 140, red);

        render_text(renderer, font, "Serveur", 340, 100, white);
        render_text(renderer, font, "WAIT", 360, 140, yellow);

        // Bouton "Continuer"
        SDL_SetRenderDrawColor(renderer, 0, 255, 0, 255); // Vert clair
        SDL_RenderFillRect(renderer, &button);
        render_text(renderer, font, "Continuer", 200, 240, white);

        // Si le bouton a été cliqué, afficher un message
        if (button_clicked) {
            render_text(renderer, font, "Action réalisée !", 180, 200, green);
        }

        SDL_RenderPresent(renderer);
    }

    // Nettoyage
    TTF_CloseFont(font);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);

    TTF_Quit();
    SDL_Quit();

    return 0;
}

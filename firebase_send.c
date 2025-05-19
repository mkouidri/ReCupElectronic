#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

// Fonction pour envoyer des données à Firebase
void send_to_firebase(const char *url, const char *data) {
    CURL *curl;
    CURLcode res;

    curl = curl_easy_init(); // Initialisation de libcurl
    if(curl) {
        // Configurer l'URL de la requête
        curl_easy_setopt(curl, CURLOPT_URL, url);

        // Configurer les données POST
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);

        // Envoyer la requête
        res = curl_easy_perform(curl);

        // Vérifier si la requête a réussi
        if(res != CURLE_OK)
            fprintf(stderr, "Erreur CURL : %s\n", curl_easy_strerror(res));
        else
            printf("Données envoyées avec succès à Firebase !\n");

        // Nettoyage
        curl_easy_cleanup(curl);
    }
}

// int main()
// {
//     // URL de votre Firebase
//     const char *firebase_url = "https://re-cup-default-rtdb.europe-west1.firebasedatabase.app/data.json";

//     // Données à envoyer (au format JSON)
//     const char *json_data = "{\"name\":\"LegoGo\", \"actual_speed\":56}";

//     // Envoyer les données à Firebase
//     send_to_firebase(firebase_url, json_data);

//     return 0;
// }

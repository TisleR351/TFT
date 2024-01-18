# Ce qu'on a fait:
- L'authentification a été mise en place
- On créé un utilisateur via l'endpoint /accounts/register avec les paramètres password, password_confirm et username dans le corps de la requête
- On récupère son token via l'endpoint /api-token-auth
- Les permissions ont été créées
- Le script pour créer les permissions est dans le MakeFile est ok.

# On doit encore:
- Mettre en place la gestion des permissions préalablement créées
- Créer les vues spécifiques
- Tester les vues des différents objets

# SignalCitoyen - Plateforme de Signalement Urbain

## 1. 🏷️ Nom et présentation du projet

**SignalCitoyen** est une application web permettant aux citoyens de signaler des problèmes urbains (dégradations, éclairage défectueux, incivilités, etc.) directement depuis leur smartphone ou ordinateur. La plateforme intègre une géolocalisation précise et un système de suivi administratif pour garantir la transparence et le traitement des signalements.

## 2. 🎯 Objectif du projet

Faciliter la remontée d'informations entre les citoyens et les services municipaux en offrant une solution intuitive, géolocalisée et transparente pour le signalement et le suivi des problèmes urbains.

## 3. 📋 Contexte

Projet développé dans le cadre du cursus EPF. La ville est confrontée à une multiplication des signalements citoyens via des canaux non structurés (réseaux sociaux, mairie, téléphone). L'objectif est de centraliser ces demandes et d'offrir un suivi clair aux citoyens.

## 4. ✨ Fonctionnalités

- **Authentification sécurisée** : Inscription et connexion avec JWT
- **Signalement** : Formulaire avec titre, description, photo (optionnelle) et géolocalisation automatique ou manuelle
- **Cartographie interactive** : Visualisation des signalements existants sur une carte Leaflet.js
- **Suivi des signalements** : Consultation du statut (En attente, En cours, Résolu)
- **Espace administrateur** : Gestion des signalements, changement de statut, suppression
- **Notifications** : (À venir) Alertes par email lors du changement de statut

## 5. 🖼️ Aperçu / Démonstration

*(À ajouter : Screenshots de l'interface, GIF démonstratif)*

## 6. 🏗️ Architecture du projet

```
Architecture Client/Serveur :

Frontend (HTML/CSS/JS) <--> API REST (FastAPI) <--> PostgreSQL (Base de données)
           │                                              │
           └── Leaflet.js (Cartographie)                  └── PostGIS (Géolocalisation)
```

## 7. 🛠️ Technologies utilisées

| Catégorie                 | Technologies                                |
| -------------------------- | ------------------------------------------- |
| **Frontend**         | HTML5, CSS3, JavaScript Vanilla, Leaflet.js |
| **Backend**          | Python 3.10+, FastAPI, SQLAlchemy ORM       |
| **Base de données** | PostgreSQL 15+, PostGIS                     |
| **Authentification** | JWT (JSON Web Tokens)                       |
| **Déploiement**     | Render (Backend), Netlify (Frontend)        |
| **Versionnement**    | Git, GitHub                                 |

## 8. 📂 Structure des fichiers

```
SignalCitoyen/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # Point d'entrée FastAPI
│   │   ├── models.py            # SQLAlchemy models
│   │   ├── schemas.py           # Pydantic schemas
│   │   ├── database.py          # Connexion PostgreSQL
│   │   ├── auth.py              # Authentification JWT
│   │   ├── config.py            # Configuration
│   │   └── routes/
│   │       ├── signalements.py  # CRUD signalements
│   │       ├── users.py         # Gestion utilisateurs
│   │       └── admin.py         # Administration
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── app.js               # Logique principale
│   │   ├── map.js               # Leaflet.js
│   │   ├── auth.js              # Login/Register
│   │   └── api.js               # Appels API
│   └── assets/
│       └── images/
│
├── docs/
│   ├── API_Documentation.md
│   └── User_Guide.md
│
├── tests/
│   ├── test_api.py
│   └── test_models.py
│
├── .env.example                  # Variables d'environnement
├── .gitignore
└── README.md
```

## 9. ⚙️ Prérequis

- Python 3.10 ou supérieur
- PostgreSQL 15 ou supérieur (ou compte Neon.tech)
- Git
- Navigateur web moderne (Chrome, Firefox, Edge)

## 10. 🚀 Installation

### Cloner le repository

```bash
git clone https://github.com/votre-username/SignalCitoyen.git
cd SignalCitoyen
```

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # ou `venv\Scripts\activate` sur Windows
pip install -r requirements.txt
```

### Frontend

Aucune installation nécessaire. Ouvrez simplement `frontend/index.html` dans votre navigateur.

## 11. 🔧 Configuration

### Variables d'environnement (fichier `.env` à la racine du backend)

```env
DATABASE_URL=postgresql://user:password@localhost:5432/signalcoyen
SECRET_KEY=votre_cle_secrete_jwt
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Création de la base de données

```sql
CREATE DATABASE signalcoyen;
CREATE EXTENSION IF NOT EXISTS postgis;
```

### Lancer les migrations (si Alembic configuré)

```bash
alembic upgrade head
```

## 12. ▶️ Utilisation

### Lancer le backend

```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

L'API sera accessible à : `http://localhost:8000`
La documentation interactive : `http://localhost:8000/docs`

### Lancer le frontend

Ouvrez `frontend/index.html` dans votre navigateur, ou utilisez un serveur local (Live Server sur VSCode).

### Comptes de test

- **Utilisateur** : `user@test.com` / `password123`
- **Admin** : `admin@test.com` / `admin123`

## 13. 📊 Données / API / Base de données

### API REST

Documentation interactive disponible sur `/docs` (Swagger).

| Méthode | Endpoint                         | Description                         |
| -------- | -------------------------------- | ----------------------------------- |
| POST     | `/api/auth/register`           | Inscription utilisateur             |
| POST     | `/api/auth/login`              | Connexion (retourne JWT)            |
| GET      | `/api/signalements`            | Liste des signalements (public)     |
| POST     | `/api/signalements`            | Créer un signalement (auth requis) |
| GET      | `/api/signalements/{id}`       | Détail d'un signalement            |
| PUT      | `/api/admin/signalements/{id}` | Mettre à jour le statut (admin)    |

### Base de données

Schéma PostgreSQL :

- `users` : id, email, nom, password_hash, role (user/admin)
- `signalements` : id, titre, description, latitude, longitude, adresse, statut, photo_url, date_creation, user_id

## 14. 🧪 Tests

```bash
cd backend
pytest tests/
```

## 15. 📈 Résultats

*(À ajouter : Métriques de performance, temps de réponse API, nombre de signalements traités)*

## 16. 🔐 Sécurité

- **Authentification JWT** : Tokens signés avec clé secrète
- **Mots de passe hachés** : Utilisation de bcrypt
- **Protection CORS** : Configuration limitée aux domaines autorisés
- **Validation des entrées** : Pydantic pour valider les données
- **SQL Injection** : Prévention via SQLAlchemy ORM

## 17. 🗺️ Roadmap

- [X] Authentification utilisateur
- [X] CRUD signalements
- [X] Cartographie interactive
- [X] Espace administrateur
- [ ] Notifications par email
- [ ] Mobile App (React Native)
- [ ] Dashboard statistiques pour la mairie
- [ ] Intégration avec des API de météo (pour les signalements liés aux conditions climatiques)

## 18. 🤝 Contribution

Les contributions sont les bienvenues ! Veuillez suivre ces étapes :

1. Fork le projet
2. Créez votre branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 19. 🐛 Problèmes connus

- La géolocalisation automatique peut échouer si les permissions du navigateur ne sont pas accordées
- Les photos sont limitées à 5MB (optimisation à venir)

## 20. 📚 Documentation / Ressources

- [Documentation FastAPI](https://fastapi.tiangolo.com/)
- [Documentation Leaflet.js](https://leafletjs.com/)
- [Documentation PostgreSQL PostGIS](https://postgis.net/documentation/)

## 21. 👤 Auteur

**[Votre Nom]** - Projet EPF

## 22. 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

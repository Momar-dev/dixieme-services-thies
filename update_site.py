import urllib.parse
import re

# 31 authentic workers from the original repository (commit 68987abd)
workers = [
    {
        'id': 1,
        'name': 'Ablaye Diallo',
        'job': 'Ouvrier BTP',
        'cat': 'btp',
        'cat_title': 'Bâtiment & BTP',
        'cat_icon': 'fa-solid fa-trowel-bricks',
        'phone': '+221778365231',
        'phone_raw': '778365231',
        'phone_clean': '221778365231',
        'phone_display': '77 836 52 31',
        'avatar_class': 'ouvrier',
        'avatar_icon': 'fa-solid fa-helmet-safety',
        'chips': ['Maçonnerie générale', 'Fondations & Dalles', 'Chantiers & Rénovation']
    },
    {
        'id': 2,
        'name': 'Aly Dieng',
        'job': 'Menuisier',
        'cat': 'btp',
        'cat_title': 'Bâtiment & Bois',
        'cat_icon': 'fa-solid fa-trowel-bricks',
        'phone': '+221775448213',
        'phone_raw': '775448213',
        'phone_clean': '221775448213',
        'phone_display': '77 544 82 13',
        'avatar_class': 'menuisier',
        'avatar_icon': 'fa-solid fa-hammer',
        'chips': ['Portes & Fenêtres', 'Meubles & Placards', 'Réparations bois']
    },
    {
        'id': 3,
        'name': 'Ada Fam',
        'job': 'BTP & Quincaillerie',
        'cat': 'btp',
        'cat_title': 'Bâtiment & Matériaux',
        'cat_icon': 'fa-solid fa-trowel-bricks',
        'phone': '+221775276967',
        'phone_raw': '775276967',
        'phone_clean': '221775276967',
        'phone_display': '77 527 69 67',
        'avatar_class': 'construction',
        'avatar_icon': 'fa-solid fa-building',
        'chips': ['Matériaux BTP', 'Quincaillerie générale', 'Fournitures chantier']
    },
    {
        'id': 4,
        'name': 'Amadou',
        'job': 'Livreur',
        'cat': 'livraison',
        'cat_title': 'Livraison Express',
        'cat_icon': 'fa-solid fa-motorcycle',
        'phone': '+221773399144',
        'phone_raw': '773399144',
        'phone_clean': '221773399144',
        'phone_display': '77 339 91 44',
        'avatar_class': 'livreur',
        'avatar_icon': 'fa-solid fa-motorcycle',
        'chips': ['Courses express', 'Colis & Marché', 'Quartier 10e & Thiès']
    },
    {
        'id': 5,
        'name': 'Agence Immobilier',
        'job': 'Immobilier',
        'cat': 'commerce',
        'cat_title': 'Commerces & Immobilier',
        'cat_icon': 'fa-solid fa-store',
        'phone': '+221774023079',
        'phone_raw': '774023079',
        'phone_clean': '221774023079',
        'phone_display': '77 402 30 79',
        'avatar_class': 'immobilier',
        'avatar_icon': 'fa-solid fa-house-chimney',
        'chips': ['Terrains titrés', 'Locations & Ventes', 'Gestion de biens']
    },
    {
        'id': 6,
        'name': 'Moussa Jakarta',
        'job': 'Livreur',
        'cat': 'livraison',
        'cat_title': 'Livraison Express',
        'cat_icon': 'fa-solid fa-motorcycle',
        'phone': '+221773500665',
        'phone_raw': '773500665',
        'phone_clean': '221773500665',
        'phone_display': '77 350 06 65',
        'avatar_class': 'livreur',
        'avatar_icon': 'fa-solid fa-motorcycle',
        'chips': ['Courses Jakarta', 'Colis urgents', 'Disponibilité 7j/7']
    },
    {
        'id': 7,
        'name': 'BARA',
        'job': 'Eau Filtrée',
        'cat': 'commerce',
        'cat_title': 'Commerces & Eau',
        'cat_icon': 'fa-solid fa-store',
        'phone': '+221771420481',
        'phone_raw': '771420481',
        'phone_clean': '221771420481',
        'phone_display': '77 142 04 81',
        'avatar_class': 'eau',
        'avatar_icon': 'fa-solid fa-droplet',
        'chips': ['Eau filtrée pure', 'Bonbonnes & Packs', 'Livraison à domicile']
    },
    {
        'id': 8,
        'name': 'Bocar Diallo',
        'job': 'Oustaz à Domicile',
        'cat': 'services',
        'cat_title': 'Services & Enseignement',
        'cat_icon': 'fa-solid fa-handshake-angle',
        'phone': '+221784000801',
        'phone_raw': '784000801',
        'phone_clean': '221784000801',
        'phone_display': '78 400 08 01',
        'avatar_class': 'oustaz',
        'avatar_icon': 'fa-solid fa-book-quran',
        'chips': ['Éducation coranique', 'Enseignement islamique', 'Cours à domicile']
    },
    {
        'id': 9,
        'name': 'Kao Soulay',
        'job': 'Plombier',
        'cat': 'btp',
        'cat_title': 'Bâtiment & Plomberie',
        'cat_icon': 'fa-solid fa-trowel-bricks',
        'phone': '+221770765473',
        'phone_raw': '770765473',
        'phone_clean': '221770765473',
        'phone_display': '77 076 54 73',
        'avatar_class': 'plombier',
        'avatar_icon': 'fa-solid fa-faucet',
        'chips': ['Réparation fuites', 'Installations sanitaires', 'Débouchage express']
    },
    {
        'id': 10,
        'name': 'Khadylaye',
        'job': 'Traiteur',
        'cat': 'services',
        'cat_title': 'Services & Traiteur',
        'cat_icon': 'fa-solid fa-handshake-angle',
        'phone': '+221772988075',
        'phone_raw': '772988075',
        'phone_clean': '221772988075',
        'phone_display': '77 298 80 75',
        'avatar_class': 'traiteur',
        'avatar_icon': 'fa-solid fa-utensils',
        'chips': ['Cuisine & Buffets', 'Cérémonies & Fêtes', 'Plats sénégalais & traiteur']
    },
    {
        'id': 11,
        'name': 'Khalilou',
        'job': 'Electricien',
        'cat': 'btp',
        'cat_title': 'Bâtiment & Électricité',
        'cat_icon': 'fa-solid fa-trowel-bricks',
        'phone': '+221773679313',
        'phone_raw': '773679313',
        'phone_clean': '221773679313',
        'phone_display': '77 367 93 13',
        'avatar_class': 'electricien',
        'avatar_icon': 'fa-solid fa-bolt',
        'chips': ['Dépannage urgent', 'Câblage & Tableaux', 'Installation éclairage']
    },
    {
        'id': 12,
        'name': 'Mamadou Ba',
        'job': 'Papeterie & Impression',
        'cat': 'commerce',
        'cat_title': 'Commerces & Bureautique',
        'cat_icon': 'fa-solid fa-store',
        'phone': '+221775175432',
        'phone_raw': '775175432',
        'phone_clean': '221775175432',
        'phone_display': '77 517 54 32',
        'avatar_class': 'papaterie',
        'avatar_icon': 'fa-solid fa-print',
        'chips': ['Photocopies & Impressions', 'Fournitures scolaires', 'Reliures de documents']
    },
    {
        'id': 13,
        'name': 'Mara Samb',
        'job': 'Commerçant (Mil, Maïs, Moulin)',
        'cat': 'commerce',
        'cat_title': 'Commerces & Céréales',
        'cat_icon': 'fa-solid fa-store',
        'phone': '+221775158090',
        'phone_raw': '775158090',
        'phone_clean': '221775158090',
        'phone_display': '77 515 80 90',
        'avatar_class': 'commercant',
        'avatar_icon': 'fa-solid fa-wheat-awn',
        'chips': ['Mil & Maïs de qualité', 'Service de moulin', 'Vente gros & détail']
    },
    {
        'id': 14,
        'name': 'Seydou Faye',
        'job': 'Menuisier Métallique',
        'cat': 'btp',
        'cat_title': 'Bâtiment & Métal',
        'cat_icon': 'fa-solid fa-trowel-bricks',
        'phone': '+221775761799',
        'phone_raw': '775761799',
        'phone_clean': '221775761799',
        'phone_display': '77 576 17 99',
        'avatar_class': 'menuisier-metal',
        'avatar_icon': 'fa-solid fa-wrench',
        'chips': ['Portes & Portails fer', 'Grilles de sécurité', 'Soudure & Ferronnerie']
    },
    {
        'id': 15,
        'name': 'Laye',
        'job': 'Frigoriste',
        'cat': 'btp',
        'cat_title': 'Froid & Climatisation',
        'cat_icon': 'fa-solid fa-snowflake',
        'phone': '+221775187352',
        'phone_raw': '775187352',
        'phone_clean': '221775187352',
        'phone_display': '77 518 73 52',
        'avatar_class': 'frigoriste',
        'avatar_icon': 'fa-solid fa-snowflake',
        'chips': ['Réparation réfrigérateurs', 'Entretien climatiseurs', 'Recharge gaz']
    },
    {
        'id': 16,
        'name': 'Diamal Oud',
        'job': 'Parfumerie',
        'cat': 'commerce',
        'img': 'a.jpeg',
        'badge_label': 'Parfumerie',
        'cat_icon': 'fa-solid fa-spray-can-sparkles',
        'phone': '+221775110304',
        'phone_raw': '775110304',
        'phone_clean': '221775110304',
        'phone_display': '77 511 03 04',
        'meta_chips': [
            '<i class="fa-brands fa-instagram" style="color: #E1306C;"></i> parfumeriediamaloud',
            '<i class="fa-brands fa-snapchat" style="color: #EAB308;"></i> diamal_oud',
            '<i class="fa-solid fa-location-dot"></i> Thiès HLM 10e'
        ]
    },
    {
        'id': 17,
        'name': 'Tima Boutique',
        'job': 'Boutique',
        'cat': 'commerce',
        'img': 'b.jpeg',
        'badge_label': 'Boutique & Mode',
        'cat_icon': 'fa-solid fa-shirt',
        'phone': '+221774582546',
        'phone_raw': '774582546',
        'phone_clean': '221774582546',
        'phone_display': '77 458 25 46',
        'meta_chips': [
            '<i class="fa-solid fa-bag-shopping"></i> Mode & Prêt-à-porter',
            '<i class="fa-solid fa-star" style="color: #F59E0B;"></i> Qualité & Nouveautés',
            '<i class="fa-solid fa-location-dot"></i> Thiès HLM 10e'
        ]
    },
    {
        'id': 18,
        'name': 'Astar Shop',
        'job': 'Boutique Alimentation',
        'cat': 'commerce',
        'is_dual': True,
        'phone': '+221770928888',
        'phone_raw': '770928888',
        'phone_clean': '221770928888',
        'phone_display': '77 092 88 88'
    },
    {
        'id': 19,
        'name': 'Daba Fall',
        'job': 'Business Shop',
        'cat': 'commerce',
        'img': 'c.jpeg',
        'badge_label': 'Business Shop',
        'cat_icon': 'fa-solid fa-store',
        'phone': '+221775433774',
        'phone_raw': '775433774',
        'phone_clean': '221775433774',
        'phone_display': '77 543 37 74',
        'meta_chips': [
            '<i class="fa-solid fa-shop"></i> Daba Business Shop',
            '<i class="fa-solid fa-gem" style="color: #EC4899;"></i> Cosmétiques & Mode',
            '<i class="fa-solid fa-location-dot"></i> Quartier Dixième, Thiès'
        ]
    },
    {
        'id': 20,
        'name': 'AGENCE SOPE SERIGNE BABACAR SY',
        'job': 'Organisation Assistance Séminaire',
        'cat': 'services',
        'img': 'd.jpeg',
        'badge_label': 'Organisation Séminaire',
        'cat_icon': 'fa-solid fa-building',
        'phone': '+221772380209',
        'phone_raw': '772380209',
        'phone_clean': '221772380209',
        'phone_display': '77 238 02 09',
        'phone_secondary': '+221339511492',
        'phone_secondary_display': '33 951 14 92',
        'meta_chips': [
            '<i class="fa-solid fa-id-card"></i> NINEA: 000433368',
            '<i class="fa-solid fa-file-contract"></i> RC: SN.THS.2000.A.1094',
            '<i class="fa-solid fa-location-dot"></i> Hlm 10ème, Villa 82-Thiès'
        ]
    },
    {
        'id': 21,
        'name': 'Alamine Business Groupe',
        'job': 'Traiteur & Organisation de Réceptions',
        'cat': 'services',
        'img': 'e.jpeg',
        'badge_label': 'Traiteur & Réceptions',
        'cat_icon': 'fa-solid fa-champagne-glasses',
        'phone': '+22176511893' if False else '+221776511893',
        'phone_raw': '776511893',
        'phone_clean': '221776511893',
        'phone_display': '77 651 18 93',
        'meta_chips': [
            '<i class="fa-solid fa-calendar-check"></i> Mariages & Cérémonies',
            '<i class="fa-solid fa-utensils"></i> Organisation réceptions',
            '<i class="fa-solid fa-location-dot"></i> Thiès et Environs'
        ]
    },
    {
        'id': 22,
        'name': 'Ameth Diokhané',
        'job': 'Electricien',
        'cat': 'btp',
        'cat_title': 'Bâtiment & Électricité',
        'cat_icon': 'fa-solid fa-trowel-bricks',
        'phone': '+221776587139',
        'phone_raw': '776587139',
        'phone_clean': '221776587139',
        'phone_display': '77 658 71 39',
        'avatar_class': 'electricien',
        'avatar_icon': 'fa-solid fa-bolt',
        'chips': ['Installations domestiques', 'Dépannage rapide', 'Disjoncteurs & Éclairage']
    },
    {
        'id': 23,
        'name': 'Cheikh Sarr',
        'job': 'Carreleur',
        'cat': 'btp',
        'cat_title': 'Bâtiment & Carrelage',
        'cat_icon': 'fa-solid fa-trowel-bricks',
        'phone': '+221774179971',
        'phone_raw': '774179971',
        'phone_clean': '221774179971',
        'phone_display': '77 417 99 71',
        'avatar_class': 'construction',
        'avatar_icon': 'fa-solid fa-border-all',
        'chips': ['Pose carrelage sol & mur', 'Faïence & Salle de bain', 'Finitions soignées']
    },
    {
        'id': 24,
        'name': 'Ndiéguéne',
        'job': 'Lavage Véhicules & Moto',
        'cat': 'services',
        'cat_title': 'Entretien & Lavage',
        'cat_icon': 'fa-solid fa-handshake-angle',
        'phone': '+221775674729',
        'phone_raw': '775674729',
        'phone_clean': '221775674729',
        'phone_display': '77 567 47 29',
        'avatar_class': 'livreur',
        'avatar_icon': 'fa-solid fa-car-side',
        'chips': ['Lavage auto complet', 'Nettoyage motos & Jakarta', 'Lavage haute pression']
    },
    {
        'id': 25,
        'name': 'Al Mountakha Travaux & Services',
        'job': 'Construction & Travaux Publics',
        'cat': 'btp',
        'cat_title': 'BTP & Travaux Publics',
        'cat_icon': 'fa-solid fa-trowel-bricks',
        'phone': '+221777288504',
        'phone_raw': '777288504',
        'phone_clean': '221777288504',
        'phone_display': '77 728 85 04',
        'avatar_class': 'construction',
        'avatar_icon': 'fa-solid fa-hard-hat',
        'chips': ['Abibou Ndiaye', 'Devis de construction', 'Pose de pavés & VRD', 'Bâtiments']
    },
    {
        'id': 26,
        'name': 'Ndéye Fatou Niang',
        'job': 'Salon de coiffure — JIGUEEN STYLE by NDF',
        'cat': 'services',
        'img': 'f.jpeg',
        'badge_label': 'Coiffure & Esthétique',
        'cat_icon': 'fa-solid fa-wand-magic-sparkles',
        'phone': '+221777622314',
        'phone_raw': '777622314',
        'phone_clean': '221777622314',
        'phone_display': '77 762 23 14',
        'meta_chips': [
            '<i class="fa-solid fa-scissors"></i> JIGUEEN STYLE by NDF',
            '<i class="fa-solid fa-heart" style="color: #E11D48;"></i> Tresses & Soins capillaires',
            '<i class="fa-solid fa-location-dot"></i> HLM 10e, Thiès'
        ]
    },
    {
        'id': 27,
        'name': 'Pape Touré',
        'job': 'Coiffeur',
        'cat': 'services',
        'cat_title': 'Beauté & Coiffure',
        'cat_icon': 'fa-solid fa-handshake-angle',
        'phone': '+221774487813',
        'phone_raw': '774487813',
        'phone_clean': '221774487813',
        'phone_display': '77 448 87 13',
        'avatar_class': 'traiteur',
        'avatar_icon': 'fa-solid fa-scissors',
        'chips': ['Coiffure hommes & enfants', 'Tailles barbe & dégradés', 'Service soigné']
    },
    {
        'id': 28,
        'name': 'Ferme Khadim Rassoul',
        'job': 'Vente Poulets, Bœufs & Moutons',
        'cat': 'commerce',
        'cat_title': 'Élevage & Boucherie',
        'cat_icon': 'fa-solid fa-store',
        'phone': '+221770979188',
        'phone_raw': '770979188',
        'phone_clean': '221770979188',
        'phone_display': '77 097 91 88',
        'avatar_class': 'commercant',
        'avatar_icon': 'fa-solid fa-cow',
        'chips': ['Poulets de chair & ponte', 'Moutons de fête & Tabaski', 'Bœufs sur commande']
    },
    {
        'id': 29,
        'name': 'Darou Bayré Construction',
        'job': 'Menuiserie Métallique',
        'cat': 'btp',
        'cat_title': 'Bâtiment & Ferronnerie',
        'cat_icon': 'fa-solid fa-trowel-bricks',
        'phone': '+221775410378',
        'phone_raw': '775410378',
        'phone_clean': '221775410378',
        'phone_display': '77 541 03 78',
        'avatar_class': 'menuisier-metal',
        'avatar_icon': 'fa-solid fa-hammer',
        'chips': ['Charpentes métalliques', 'Portes fer & grilles', 'Ferronnerie générale']
    },
    {
        'id': 30,
        'name': 'Entreprise Mini Forage',
        'job': 'Forages',
        'cat': 'btp',
        'cat_title': 'Hydraulique & Forages',
        'cat_icon': 'fa-solid fa-trowel-bricks',
        'phone': '+221773567118',
        'phone_raw': '773567118',
        'phone_clean': '221773567118',
        'phone_display': '77 356 71 18',
        'avatar_class': 'construction',
        'avatar_icon': 'fa-solid fa-water',
        'chips': ['Forages d\'eau potable', 'Installation pompes', 'Maintenance puits & forages']
    },
    {
        'id': 31,
        'name': 'Fall Business',
        'job': 'Assurance & Cosmétiques',
        'cat': 'commerce',
        'cat_title': 'Assurance & Beauté',
        'cat_icon': 'fa-solid fa-store',
        'phone': '+221779979969',
        'phone_raw': '779979969',
        'phone_clean': '221779979969',
        'phone_display': '77 997 99 69',
        'avatar_class': 'immobilier',
        'avatar_icon': 'fa-solid fa-shield-halved',
        'chips': ['Conseil & Assurance', 'Produits cosmétiques', 'Soins & bien-être']
    }
]

def render_worker_card(w, index):
    stagger = (index % 6) + 1
    encoded_name = urllib.parse.quote(w['name'])
    
    if w.get('is_dual'):
        return f'''            <!-- Worker {w['id']}: {w['name']} (DUAL-FRAME j.jpeg & i.jpeg) -->
            <div class="worker-card with-image animate-on-scroll stagger-{stagger}" data-category="commerce">
                <div class="image-frame dual-image-frame">
                    <div class="dual-thumb" onclick="openLightbox('j.jpeg', 'Astar Shop', 'Boutique Alimentation — By Dykha', '+221770928888')">
                        <img src="j.jpeg" alt="Astar Shop - Logo" class="worker-image">
                        <span class="dual-badge"><i class="fa-solid fa-expand"></i> Enseigne</span>
                    </div>
                    <div class="dual-thumb" onclick="openLightbox('i.jpeg', 'Astar Shop', 'Boutique Alimentation — By Dykha', '+221770928888')">
                        <img src="i.jpeg" alt="Astar Shop - Produits" class="worker-image">
                        <span class="dual-badge"><i class="fa-solid fa-expand"></i> Ravitaillement</span>
                    </div>
                    <span class="card-badge-pill"><i class="fa-solid fa-basket-shopping"></i> Alimentation</span>
                </div>
                <div class="card-body">
                    <div class="card-header-info">
                        <h3>Astar Shop</h3>
                        <span class="worker-job-pill">Boutique Alimentation</span>
                    </div>
                    <div class="meta-chips-grid">
                        <span class="meta-chip"><i class="fa-solid fa-crown" style="color: #F59E0B;"></i> By Dykha</span>
                        <span class="meta-chip"><i class="fa-brands fa-whatsapp" style="color: #25D366;"></i> Commandes WhatsApp</span>
                        <span class="meta-chip"><i class="fa-solid fa-truck-fast"></i> Livraison possible</span>
                    </div>
                    <div class="worker-trust-strip">
                        <span class="trust-status-pill"><span class="dot"></span> Disponible</span>
                        <span class="trust-badge-response"><i class="fa-regular fa-clock"></i> Réponse rapide</span>
                    </div>
                    <div class="worker-actions">
                        <a href="tel:+221770928888" class="btn-primary-call" onclick="showToast('Appel à Astar Shop...')">
                            <i class="fa-solid fa-phone"></i> 77 092 88 88
                        </a>
                        <button class="copy-phone-btn" onclick="copyPhone('770928888')" title="Copier le numéro" aria-label="Copier le numéro d'Astar Shop">
                            <i class="fa-regular fa-copy"></i>
                        </button>
                        <a href="https://wa.me/221770928888?text=Bonjour%20Astar%20Shop,%20je%20vous%20contacte%20via%20Dixième%20Services." target="_blank" rel="noopener noreferrer" class="whatsapp-btn" title="Contacter sur WhatsApp" onclick="showToast('Ouverture WhatsApp...')">
                            <i class="fa-brands fa-whatsapp"></i>
                        </a>
                    </div>
                </div>
            </div>'''
    
    elif w.get('img'):
        chips_html = '\n'.join([f'                        <span class="meta-chip">{c}</span>' for c in w['meta_chips']])
        secondary_btn = ''
        if w.get('phone_secondary'):
            secondary_btn = f'''
                        <a href="tel:{w['phone_secondary']}" class="btn-secondary-call" onclick="showToast('Appel fixe...')" title="Appeler le fixe">
                            <i class="fa-solid fa-phone-volume"></i> {w['phone_secondary_display']}
                        </a>'''
        return f'''            <!-- Worker {w['id']}: {w['name']} (IMAGE {w['img']}) -->
            <div class="worker-card with-image animate-on-scroll stagger-{stagger}" data-category="{w['cat']}">
                <div class="image-frame">
                    <img src="{w['img']}" alt="" class="image-blur-bg" aria-hidden="true">
                    <img src="{w['img']}" alt="{w['name']}" class="worker-image">
                    <span class="card-badge-pill"><i class="{w['cat_icon']}"></i> {w['badge_label']}</span>
                    <button class="image-preview-btn" onclick="openLightbox('{w['img']}', '{w['name']}', '{w['job']}', '{w['phone']}')" title="Agrandir l'image" aria-label="Agrandir la photo de {w['name']}">
                        <i class="fa-solid fa-expand"></i>
                    </button>
                </div>
                <div class="card-body">
                    <div class="card-header-info">
                        <h3>{w['name']}</h3>
                        <span class="worker-job-pill">{w['job']}</span>
                    </div>
                    <div class="meta-chips-grid">
{chips_html}
                    </div>
                    <div class="worker-trust-strip">
                        <span class="trust-status-pill"><span class="dot"></span> Disponible</span>
                        <span class="trust-badge-response"><i class="fa-regular fa-clock"></i> Réponse rapide</span>
                    </div>
                    <div class="worker-actions">
                        <a href="tel:{w['phone']}" class="btn-primary-call" onclick="showToast('Appel à {w['name']}...')">
                            <i class="fa-solid fa-phone"></i> {w['phone_display']}
                        </a>
                        <button class="copy-phone-btn" onclick="copyPhone('{w['phone_raw']}')" title="Copier le numéro" aria-label="Copier le numéro de {w['name']}">
                            <i class="fa-regular fa-copy"></i>
                        </button>
                        <a href="https://wa.me/{w['phone_clean']}?text=Bonjour%20{encoded_name},%20je%20vous%20contacte%20via%20Dixième%20Services." target="_blank" rel="noopener noreferrer" class="whatsapp-btn" title="Contacter sur WhatsApp" onclick="showToast('Ouverture WhatsApp...')">
                            <i class="fa-brands fa-whatsapp"></i>
                        </a>{secondary_btn}
                    </div>
                </div>
            </div>'''
            
    else:
        chips_html = '\n'.join([f'                        <span class="specialty-chip">{c}</span>' for c in w['chips']])
        return f'''            <!-- Worker {w['id']}: {w['name']} -->
            <div class="worker-card animate-on-scroll stagger-{stagger}" data-category="{w['cat']}">
                <div class="worker-card-cover">
                    <span class="card-cat-badge"><i class="{w['cat_icon']}"></i> {w['cat_title']}</span>
                    <span class="card-verified-tag"><i class="fa-solid fa-circle-check"></i> Vérifié</span>
                </div>
                <div class="worker-card-body">
                    <div class="worker-avatar-wrap">
                        <div class="worker-avatar {w['avatar_class']}">
                            <i class="{w['avatar_icon']}"></i>
                        </div>
                        <span class="avatar-live-indicator" title="Disponible"></span>
                    </div>
                    <h3>{w['name']}</h3>
                    <div class="worker-role-line">
                        <span class="worker-job-badge">{w['job']}</span>
                        <span class="worker-location-tag"><i class="fa-solid fa-location-dot"></i> Quartier 10e</span>
                    </div>
                    <div class="worker-specialties-list">
{chips_html}
                    </div>
                    <div class="worker-trust-strip">
                        <span class="trust-status-pill"><span class="dot"></span> Disponible</span>
                        <span class="trust-badge-response"><i class="fa-regular fa-clock"></i> Réponse rapide</span>
                    </div>
                    <div class="worker-actions">
                        <a href="tel:{w['phone']}" class="btn-primary-call" onclick="showToast('Appel à {w['name']}...')">
                            <i class="fa-solid fa-phone"></i> {w['phone_display']}
                        </a>
                        <button class="copy-phone-btn" onclick="copyPhone('{w['phone_raw']}')" title="Copier le numéro" aria-label="Copier le numéro de {w['name']}">
                            <i class="fa-regular fa-copy"></i>
                        </button>
                        <a href="https://wa.me/{w['phone_clean']}?text=Bonjour%20{encoded_name},%20je%20vous%20contacte%20via%20Dixième%20Services." target="_blank" rel="noopener noreferrer" class="whatsapp-btn" title="Contacter sur WhatsApp" onclick="showToast('Ouverture WhatsApp...')">
                            <i class="fa-brands fa-whatsapp"></i>
                        </a>
                    </div>
                </div>
            </div>'''

rendered_cards = '\n\n'.join([render_worker_card(w, i) for i, w in enumerate(workers)])

# Count categories
btp_count = sum(1 for w in workers if w['cat'] == 'btp')
livraison_count = sum(1 for w in workers if w['cat'] == 'livraison')
commerce_count = sum(1 for w in workers if w['cat'] == 'commerce')
services_count = sum(1 for w in workers if w['cat'] == 'services')

print(f'Total workers rendered: {len(workers)}')
print(f'BTP: {btp_count}, Livraison: {livraison_count}, Commerce: {commerce_count}, Services: {services_count}')

# Read modern template
with open('index_modern_template.html') as f:
    mod_html = f.read()

# Replace the entire <section id="workers">...</section>
workers_section_new = f'''    <!-- Annuaire des Professionnels -->
    <section id="workers" aria-labelledby="workers-heading">
        <div class="section-header-center animate-on-scroll">
            <div class="pill-badge pill-red">
                <i class="fa-solid fa-address-book"></i>
                <span>Annuaire Local & Artisans</span>
            </div>
            <h2 id="workers-heading" class="heading">Nos Professionnels du Quartier</h2>
            <p class="heading-sub">
                Des artisans, commerçants et spécialistes qualifiés, immédiatement joignables par appel direct ou WhatsApp.
            </p>
        </div>

        <!-- Filter & Search Bar -->
        <div class="filter-search-container animate-on-scroll stagger-1">
            <div class="search-bar-wrapper">
                <i class="fa-solid fa-magnifying-glass" aria-hidden="true"></i>
                <input type="text" id="workerSearch" class="search-input" placeholder="Rechercher par nom, métier ou activité (ex: Plombier, Ablaye, Électricien, Astar Shop...)" aria-label="Rechercher un professionnel">
            </div>

            <div class="tab-buttons" role="tablist" aria-label="Filtrer par catégorie">
                <button class="tab-btn active" data-filter="all" role="tab" aria-selected="true">
                    Tous <span class="badge-count">{len(workers)}</span>
                </button>
                <button class="tab-btn" data-filter="btp" role="tab" aria-selected="false">
                    <i class="fa-solid fa-hammer"></i> Bâtiment & BTP <span class="badge-count">{btp_count}</span>
                </button>
                <button class="tab-btn" data-filter="livraison" role="tab" aria-selected="false">
                    <i class="fa-solid fa-motorcycle"></i> Livraison <span class="badge-count">{livraison_count}</span>
                </button>
                <button class="tab-btn" data-filter="commerce" role="tab" aria-selected="false">
                    <i class="fa-solid fa-shop"></i> Commerce <span class="badge-count">{commerce_count}</span>
                </button>
                <button class="tab-btn" data-filter="services" role="tab" aria-selected="false">
                    <i class="fa-solid fa-handshake-angle"></i> Services & Divers <span class="badge-count">{services_count}</span>
                </button>
            </div>
        </div>

        <!-- Workers Grid -->
        <div class="workers-grid" id="workersGrid">
{rendered_cards}
        </div>
    </section>'''

# Clean replacement of section#workers
w_start = mod_html.find('<section id="workers"')
w_end = mod_html.find('</section>', mod_html.find('<div class="workers-grid" id="workersGrid">')) + len('</section>')
mod_html = mod_html[:w_start] + workers_section_new + mod_html[w_end:]

# Replace services section with the 6 exact original services with modern design
services_new_section = '''    <!-- Services Section -->
    <section id="services" aria-labelledby="services-heading">
        <div class="section-header-center animate-on-scroll">
            <div class="pill-badge pill-emerald">
                <i class="fa-solid fa-cubes-stacked"></i>
                <span>Pôles Clés du Quartier</span>
            </div>
            <h2 id="services-heading" class="heading">Nos Services de Proximité</h2>
            <p class="heading-sub">
                Des solutions rapides, fiables et coordonnées par la direction du Quartier Dixième pour répondre à tous vos besoins quotidiens.
            </p>
        </div>

        <div class="services-grid">
            <!-- Service 1: Pharmacie de garde -->
            <div class="service-card animate-on-scroll stagger-1">
                <div class="img-container">
                    <img src="https://images.unsplash.com/photo-1587854692152-cbe660dbde88?q=80&w=800&auto=format&fit=crop" alt="Pharmacie de garde au Quartier Dixième" loading="lazy">
                    <div class="icon-overlay green"><i class="fa-solid fa-prescription-bottle-medical"></i></div>
                </div>
                <div class="card-content">
                    <h3>Pharmacie de garde</h3>
                    <p>Service de livraison de médicaments à domicile. Commandez vos médicaments et recevez-les rapidement chez vous.</p>
                    <div class="card-footer">
                        <a href="tel:+221772133398" class="contact-link" onclick="showToast('Appel permanence pharmacie...')">
                            Contacter <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Service 2: Immobilier -->
            <div class="service-card animate-on-scroll stagger-2">
                <div class="img-container">
                    <img src="https://keurcity.com/wp-content/uploads/2021/10/Location-bien-immobilier-Senegal.jpg" alt="Immobilier et Terrains au Quartier Dixième" loading="lazy">
                    <div class="icon-overlay purple"><i class="fa-solid fa-house-chimney"></i></div>
                </div>
                <div class="card-content">
                    <h3>Immobilier</h3>
                    <p>Terrains et maisons à vendre dans le quartier. Trouvez la propriété de vos rêves avec notre accompagnement personnalisé.</p>
                    <div class="card-footer">
                        <a href="tel:+221772133398" class="contact-link" onclick="showToast('Appel service immobilier...')">
                            Contacter <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Service 3: Livraison -->
            <div class="service-card animate-on-scroll stagger-3">
                <div class="img-container">
                    <img src="livraison_express_thies.jpg" alt="Service de livraison rapide par moto au Quartier Dixième" loading="lazy">
                    <div class="icon-overlay orange"><i class="fa-solid fa-motorcycle"></i></div>
                </div>
                <div class="card-content">
                    <h3>Livraison</h3>
                    <p>Service de livraison rapide par moto. Vos colis livrés en un temps record partout dans le quartier et ses environs.</p>
                    <div class="card-footer">
                        <a href="tel:+221772133398" class="contact-link" onclick="showToast('Appel service livraison...')">
                            Contacter <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Service 4: Plomberie -->
            <div class="service-card animate-on-scroll stagger-4">
                <div class="img-container">
                    <img src="https://images.unsplash.com/photo-1504148455328-c376907d081c?w=600&auto=format&fit=crop&q=80" alt="Intervention plomberie d'urgence au Quartier Dixième" loading="lazy">
                    <div class="icon-overlay blue"><i class="fa-solid fa-faucet"></i></div>
                </div>
                <div class="card-content">
                    <h3>Plomberie</h3>
                    <p>Intervention rapide pour toute fuite, réparation de chauffe-eau ou installation sanitaire dans votre domicile.</p>
                    <div class="card-footer">
                        <a href="tel:+221772133398" class="contact-link" onclick="showToast('Appel service plomberie...')">
                            Contacter <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Service 5: Électricité -->
            <div class="service-card animate-on-scroll stagger-5">
                <div class="img-container">
                    <img src="https://images.unsplash.com/photo-1621905251189-08b45d6a269e?w=600&auto=format&fit=crop&q=80" alt="Dépannage électricité au Quartier Dixième" loading="lazy">
                    <div class="icon-overlay yellow"><i class="fa-solid fa-bolt"></i></div>
                </div>
                <div class="card-content">
                    <h3>Électricité</h3>
                    <p>Dépannage électrique, installation de prises, réparation de court-circuit et mise aux normes de votre installation.</p>
                    <div class="card-footer">
                        <a href="tel:+221772133398" class="contact-link" onclick="showToast('Appel service électricité...')">
                            Contacter <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Service 6: Location de Voiture -->
            <div class="service-card animate-on-scroll stagger-6">
                <div class="img-container">
                    <img src="https://yiricar.com/wp-content/uploads/2024/02/FORD-FUSION-TITANIUM-1.jpg" alt="Location de véhicules à Thiès et environs" loading="lazy">
                    <div class="icon-overlay red-icon"><i class="fa-solid fa-car"></i></div>
                </div>
                <div class="card-content">
                    <h3>Location de Voiture</h3>
                    <p>Location de véhicules pour vos déplacements personnels ou professionnels à Thiès et ses environs.</p>
                    <div class="card-footer">
                        <a href="tel:+221772133398" class="contact-link" onclick="showToast('Appel location véhicule...')">
                            Contacter <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>'''

# Replace services section
s_start = mod_html.find('<section id="services"')
s_end = mod_html.find('</section>', s_start) + len('</section>')
mod_html = mod_html[:s_start] + services_new_section + mod_html[s_end:]

# Update stats in hero to 31
mod_html = re.sub(r'<div class="stat-number">28\+?</div>\s*<div class="stat-label">Artisans & Pros Vérifiés</div>',
                 '<div class="stat-number">31</div>\n                <div class="stat-label">Professionnels Répertoriés</div>',
                 mod_html)

# Update footer services links to match original
footer_services_orig = '''                    <ul class="footer-links">
                        <li><a href="#services"><i class="fa-solid fa-chevron-right"></i> Pharmacie de garde</a></li>
                        <li><a href="#services"><i class="fa-solid fa-chevron-right"></i> Immobilier</a></li>
                        <li><a href="#services"><i class="fa-solid fa-chevron-right"></i> Livraison express</a></li>
                        <li><a href="#services"><i class="fa-solid fa-chevron-right"></i> Plomberie</a></li>
                        <li><a href="#services"><i class="fa-solid fa-chevron-right"></i> Électricité</a></li>
                        <li><a href="#services"><i class="fa-solid fa-chevron-right"></i> Location de Voiture</a></li>
                    </ul>'''

f_start = mod_html.find('<ul class="footer-links">')
f_end = mod_html.find('</ul>', f_start) + len('</ul>')
mod_html = mod_html[:f_start] + footer_services_orig + mod_html[f_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(mod_html)

print('Updated index.html successfully!')

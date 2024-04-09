
#include <SFML/Window/Event.hpp>

#include "./ext-geometry.hpp"



mvt_chp_pesanteur::MouvementChampPesenteur::MouvementChampPesenteur(){
    std::string volume_abs_path("/Users/ibrahimatraore/COURSES/API_PHYSICS/images/");
    //std::string path = volume_abs_path + std::string("projection_vecteur.svg");
    this->counter = -1;

    /* Create image */
    //sfc::SVGImage img;

    /* Don't show debug lines */
    //img.setMode(sfc::DrawMode::NORMAL);

    /* Load SVG image from file */
    //img.loadFromFile(path);

    /* Rasterize image & save it to file */
    //img.rasterize().saveToFile(volume_abs_path + std::string("image.png"));

    /* Move it by [10, 10] to make it more visible */
    //img.move(sf::Vector2f(70, 80));
    
    /// WINDOW: 0
    this->containerTexture_vector[++this->counter] = sf::Texture();
    if( this->containerTexture_vector[this->counter].loadFromFile(volume_abs_path + std::string("les_titres.png")) ){ 
        this->sprit_img_containers[this->counter] = sf::Sprite(this->containerTexture_vector[ this->counter ]);
        this->sprit_img_containers[this->counter].setPosition(sf::Vector2f(WIDTH/2 + 136, 70.f)); // absolute position
    }else {
        std::cout << "Impossible de charger video animation\n"; exit(1);
    } 

    
    
    /// WINDOW: 1
    this->containerTexture_vector[++this->counter] = sf::Texture();
    if( this->containerTexture_vector[this->counter].loadFromFile(volume_abs_path + std::string("I_proj_vec.png")) ){ 
        this->sprit_img_containers[this->counter] = sf::Sprite(this->containerTexture_vector[ this->counter ]);
        this->sprit_img_containers[this->counter].setPosition(sf::Vector2f(100, 50.f)); // absolute position
    }else {
        std::cout << "Impossible de charger video animation\n"; exit(1);
    } 

    //Add sprites infos to screenAndHisSpritesPositions (from screen class)
    // It will help us to manage dynamic eraser color
    sc.addSpriteInfosToSuitableScreen(1, this->sprit_img_containers[this->counter]);
    //---------------------------------------------------------------------//


    //EXO1: /// WINDOW: 2
    this->containerTexture_vector[++this->counter] = sf::Texture();
    if( this->containerTexture_vector[this->counter].loadFromFile(volume_abs_path + std::string("I_exo1.png")) ){ 
        this->sprit_img_containers[this->counter] = sf::Sprite(this->containerTexture_vector[ this->counter ]);
        this->sprit_img_containers[this->counter].setPosition(sf::Vector2f(100, 50.f)); // absolute position
    }else {
        std::cout << "Impossible de charger I_exo1.png\n"; exit(1);
    }

    //Add sprites infos to screenAndHisSpritesPositions (from screen class)
    // It will help us to manage dynamic eraser color
    sc.addSpriteInfosToSuitableScreen(2, this->sprit_img_containers[this->counter]);
    //---------------------------------------------------------------------//

    //DERIVEE PRIMITIVE: /// WINDOW: 3
    this->containerTexture_vector[++this->counter] = sf::Texture();
    if( this->containerTexture_vector[this->counter].loadFromFile(volume_abs_path + std::string("II_dev_prim.png")) ){ 
        this->sprit_img_containers[this->counter] = sf::Sprite(this->containerTexture_vector[this->counter]);
        this->sprit_img_containers[this->counter].setPosition(sf::Vector2f(100, 50.f)); // absolute position
    }else {
        std::cout << "Impossible de charger II_dev_prim.png\n"; exit(1);
    } 

    //Add sprites infos to screenAndHisSpritesPositions (from screen class)
    // It will help us to manage dynamic eraser color
    sc.addSpriteInfosToSuitableScreen(3, this->sprit_img_containers[this->counter]);
    //---------------------------------------------------------------------//


    //EXO - DERIVEE PRIMITIVE: /// WINDOW: 4
    this->containerTexture_vector[++this->counter] = sf::Texture();
    if( this->containerTexture_vector[this->counter].loadFromFile(volume_abs_path + std::string("II_exo2.png")) ){ 
        this->sprit_img_containers[this->counter] = sf::Sprite(this->containerTexture_vector[this->counter]);
        this->sprit_img_containers[this->counter].setPosition(sf::Vector2f(100, 50.f)); // absolute position
    }else {
        std::cout << "Impossible de charger II_dev_prim.png\n"; exit(1);
    } 

    //Add sprites infos to screenAndHisSpritesPositions (from screen class)
    // It will help us to manage dynamic eraser color
    sc.addSpriteInfosToSuitableScreen(4, this->sprit_img_containers[this->counter]);
    //---------------------------------------------------------------------//


    //EXO - DERIVEE PRIMITIVE /// WINDOW: 5
    /*this->containerTexture_vector[++this->counter] = sf::Texture();
    if( this->containerTexture_vector[this->counter].loadFromFile(volume_abs_path + std::string("II_exo2.png")) ){ 
        this->sprit_img_containers[this->counter] = sf::Sprite(this->containerTexture_vector[this->counter]);
        this->sprit_img_containers[this->counter].setPosition(sf::Vector2f(WIDTH/2 + 90, 80.f)); // absolute position
    }else {
        std::cout << "Impossible de charger II_dev_prim.png"; exit(1);
    } */

    //EXO - DERIVEE PRIMITIVE /// WINDOW: 6
        ++this->counter; //[because the previous course will tabke two windows]
    this->containerTexture_vector[++this->counter] = sf::Texture();
    if( this->containerTexture_vector[this->counter].loadFromFile(volume_abs_path + std::string("les_etudes.png")) ){ 
        this->sprit_img_containers[this->counter] = sf::Sprite(this->containerTexture_vector[this->counter]);
        this->sprit_img_containers[this->counter].setPosition(sf::Vector2f(100, 50.f)); // absolute position
    }else {
        std::cout << "Impossible de charger II_dev_prim.png\n"; exit(1);
    } 

    //Add sprites infos to screenAndHisSpritesPositions (from screen class)
    // It will help us to manage dynamic eraser color
    sc.addSpriteInfosToSuitableScreen(6, this->sprit_img_containers[this->counter]);
    //---------------------------------------------------------------------//


    //LES ETUDES /// WINDOW: 7
    this->containerTexture_vector[++this->counter] = sf::Texture();
    if( this->containerTexture_vector[this->counter].loadFromFile(volume_abs_path + std::string("les_etudes.png")) ){ 
        this->sprit_img_containers[this->counter] = sf::Sprite(this->containerTexture_vector[this->counter]);
        this->sprit_img_containers[this->counter].setPosition(sf::Vector2f(100, 50.f)); // absolute position
    }else {
        std::cout << "Impossible de charger II_dev_prim.png\n"; exit(1);
    } 

    //Add sprites infos to screenAndHisSpritesPositions (from screen class)
    // It will help us to manage dynamic eraser color
    sc.addSpriteInfosToSuitableScreen(7, this->sprit_img_containers[this->counter]);
    //---------------------------------------------------------------------//

    //SUJETS BAC /// WINDOW: 8
    this->containerTexture_vector[++this->counter] = sf::Texture();
    if( this->containerTexture_vector[this->counter].loadFromFile(volume_abs_path + std::string("sujet_bac.png")) ){ 
        this->sprit_img_containers[this->counter] = sf::Sprite(this->containerTexture_vector[this->counter]);
        this->sprit_img_containers[this->counter].setPosition(sf::Vector2f(100, 50.f)); // absolute position
    }else {
        std::cout << "Impossible de charger II_dev_prim.png"; exit(1);
    } 
}


 mvt_chp_pesanteur::MouvementChampPesenteur::~MouvementChampPesenteur(){

 }





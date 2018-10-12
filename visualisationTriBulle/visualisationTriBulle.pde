float[] listeValeurs;
int i = 0;
int j = 0;
int L = 0;
int nombreValeurs = 30;
float largeur;

void setup(){
  
 fullScreen();
 stroke(0);
 fill(0);
 
 listeValeurs = new float[nombreValeurs];
 
 for(int i=0; i < listeValeurs.length; i++){
  
   listeValeurs[i] = random(height);
   
 }
 
 L = listeValeurs.length;
 
 largeur = width/nombreValeurs;
 
}

void draw(){
  
 background(150,150,150);
 afficherListe(listeValeurs);
 
 float a = listeValeurs[j];
 float b = listeValeurs[j+1];
 
 if(a>b){
  
   echanger(listeValeurs,j,j+1);
   
 }
 
 if(j>(L-i-3)){
  
   j = -1;
   i = i+1;
   
 }
 
 if(i > L - 1){
  
   noLoop();
   
 }
 
 j = j+1;
 
}

void afficherListe(float[] l){
  
  for(int i=0; i < l.length; i++){
  
    rect(i*largeur,0,largeur,height - l[i]);
   
  }
  
}

void echanger(float[] l, int i1, int i2){
  
  float aux = l[i1];
  l[i1] = l[i2];
  l[i2] = aux;
  
}

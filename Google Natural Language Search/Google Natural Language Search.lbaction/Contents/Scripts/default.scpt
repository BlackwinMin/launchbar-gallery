JsOsaDAS1.001.00bplist00�Vscripto+ f u n c t i o n   h a n d l e _ s t r i n g ( s e a r c h Q u e r y )   { 
 / /h�g�e�gS�ep 
 v a r   r e g D a t e   =   / \ s [ y | m | w | d | h | n ] [ 0 - 9 ] + / 
 i f   ( r e g D a t e . e x e c ( s e a r c h Q u e r y ) ) { 
 	 v a r   d a t e Q u e r y   =   " & t b s = q d r : "   +   r e g D a t e . e x e c ( s e a r c h Q u e r y ) . j o i n ( ) . s u b s t r i n g ( 1 ) 
 } 
 e l s e   { 
 	 v a r   d a t e Q u e r y   =   " " 
 } 
 
 / /h�g�e�g�V�S�ep 
 v a r   r e g D a t e r a n g e   =   / \ s [ 0 - 9 ] { 4 } - [ 0 - 9 ] { 2 } - [ 0 - 9 ] { 2 } / g 
 i f   ( s e a r c h Q u e r y . m a t c h ( r e g D a t e r a n g e ) ) { 
 	 v a r   d a t e r a n g e Q u e r y t e m p a r r a y   =   s e a r c h Q u e r y . m a t c h ( r e g D a t e r a n g e ) 
 	 v a r   d a t e r a n g e Q u e r y t e m p s t a r t   =   d a t e r a n g e Q u e r y t e m p a r r a y [ 0 ] . s u b s t r i n g ( 1 ) 
 	 v a r   d a t e r a n g e Q u e r y t e m p e n d   =   d a t e r a n g e Q u e r y t e m p a r r a y [ 1 ] . s u b s t r i n g ( 1 ) 
 	 v a r   d a t e r a n g e Q u e r y   =   " a f t e r : "   +   d a t e r a n g e Q u e r y t e m p s t a r t   +   "   b e f o r e : "   +   d a t e r a n g e Q u e r y t e m p e n d 
 } 
 e l s e   { 
 	 v a r   d a t e r a n g e Q u e r y   =   " " 
 } 
 
 / /h�g�� S�ep 
 v a r   r e g L a n g u a g e C N   =   / \ sN-e� / 
 v a r   r e g L a n g u a g e E N   =   / \ s��e� / 
 i f   ( s e a r c h Q u e r y . m a t c h ( r e g L a n g u a g e C N ) ) { 
 	 v a r   l a n g Q u e r y   =   " & l r = l a n g _ z h - C N " 
 } 
 e l s e   i f   ( s e a r c h Q u e r y . m a t c h ( r e g L a n g u a g e E N ) ) { 
 	 v a r   l a n g Q u e r y   =   " & l r = l a n g _ e n " 
 } 
 e l s e   { 
 	 v a r   l a n g Q u e r y   =   " " 
 } 
 
 v a r   p u r e Q u e r y   =   s e a r c h Q u e r y . r e p l a c e ( r e g D a t e , ' ' ) . r e p l a c e ( r e g D a t e r a n g e ,   ' ' ) . r e p l a c e ( r e g L a n g u a g e C N , ' ' ) . r e p l a c e ( r e g L a n g u a g e E N , ' ' ) 
 
 v a r   s e a r c h U R L   =   " h t t p s : / / w w w . g o o g l e . h k / s e a r c h ? q = "   +   d a t e r a n g e Q u e r y   +   p u r e Q u e r y   +   d a t e Q u e r y   +   l a n g Q u e r y 
 l e t   e n c o d e U R I _ u r l   =   e n c o d e U R I ( s e a r c h U R L ) 
 
 v a r   S a f a r i   =   A p p l i c a t i o n ( " S a f a r i " ) ; 
 v a r   d o c   =   S a f a r i . D o c u m e n t ( ) . m a k e ( ) ; 
 v a r   w i n   =   S a f a r i . w i n d o w s [ d o c . n a m e ( ) ] ; 
 w i n . c u r r e n t T a b . u r l   =   e n c o d e U R I _ u r l 
 }                              
ljscr  ��ޭ
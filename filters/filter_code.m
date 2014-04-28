%LOW PASS
f= [0 (4000-200)/44100 4000/44100 (4000+200)/44100 1];
u= [1 1 0.1 0.01 0.01];
h= fir2(100,f,u);
plot(h)
save('low4000.txt','h','-ascii')
type('low4000.txt')
%%
%LOW PASS 2
f= [0 (900-100)/44100 900/44100 (900+100)/44100 1];
u= [1 1 0.1 0.01 0.01];
h= fir2(100,f,u);
plot(h)
save('low900.txt','h','-ascii')
type('low900.txt')
%%
%HIGH PASS
f= [0 (900-100)/44100 900/44100 (900+100)/44100 1];
u= [0.01 0.01 0.1 1 1];
h= fir2(150,f,u);
plot(h)
save('high300.txt','h','-ascii')
type('high300.txt')

%%
f = [0 200/44100 500/44100 1];            % Band edges in pairs
a = [0 1 1 0];            % Highpass filter amplitude
b = fir2(100,f,a);
plot(b)
save('band200500.txt','h','-ascii')
type('band200500.txt')

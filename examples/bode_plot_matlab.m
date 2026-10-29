% Bode plot for
% H(s) = 10(1 + s/10) / [(1 + s)(1 + s/100)]
%
% Requires MATLAB Control System Toolbox.

s = tf('s');
H = 10*(1 + s/10)/((1 + s)*(1 + s/100));

% Use a logarithmic frequency grid from 0.1 to 1000 rad/s.
w = logspace(-1, 3, 1000);

figure;
bode(H, w);
grid on;

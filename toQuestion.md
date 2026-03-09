function X = myradix2dft(x)
% MYRADIX2DFT radix-2 discrete Fourier transform
    np = length(x); % must be a power of two
    if np == 1
        X = x;
    else
        xe = x(1:2:end);
        xo = x(2:2:end);
        xe = myradix2dft(xe);
        xo = myradix2dft(xo);
        omega = exp(-2*pi*1i/np);
        k = (0:(np/2-1))';
        w = omega.^k;
        xo = w.*xo;
        X = [xe+xo; xe-xo];
    end
end
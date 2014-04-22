%training
trainingInput = [1.34992203659 7.74395452897;0.182872465258 0.695174136689;0.369750953973 0.899374981456;2.85565999232 5.56048926544;0.996772236728 8.67120364142;];
trainingOutput = [-0.872983453297 0.505929776655 0.730762609532 -0.603019365928 -0.813887127328 ];
trainingInput = transpose(trainingInput);
%testing
testingInput = [1.52023951505 5.34377048481;3.4615159875 5.60174366378;1.25451945952 6.52658838993;4.77342411789 2.68151155104;3.93239922795 3.89938958488;2.26369114449 2.95447570511;1.53199307631 4.22992958372;0.512963509552 8.98787339968;1.23985922258 5.41177073209;2.79856355129 1.10072109944;2.31798552552 6.12660660451;2.84784459002 6.51261078446;1.10984407376 8.09536355219;0.797868793179 5.41495758885;1.32075111986 0.939566721613;4.45281856454 1.16804511585;3.54020391972 4.19953218778;4.53313935534 3.09933227257;2.92994043834 4.26266644303;3.0540637991 0.737008269502;];
testingOutput = [-0.867687862261 -0.0207959885509 -0.981129868711 -0.168202016513 -0.390423251924 -0.564094609703 -0.484127034531 -0.956944133233 -0.720242580496 -0.20584923379 -0.784504370754 -0.178080400786 -0.902551740399 -0.355785972387 0.975954558457 -0.947825520035 -0.599771323317 -0.199041560986 -0.939754569471 -0.277292815387 ];
testingInput = transpose(testingInput);
%Parameters set dynamically
hiddenNodes = 10;
epochs = 1500;
etta = 0.07;
neuralType = 'traingd';
epsilon = 0.1;

%Set net
net = feedforwardnet(hiddenNodes);  %Set neuronal net with N hidden nodes
net.trainFcn = neuralType;
net.trainParam.goal = epsilon      %Set epsilon
net.trainParam.epochs = epochs;    %Set epochs
net.trainParam.lr = etta;          %Set etta

net = train(net,trainingInput,trainingOutput);
view(net)
netTestingOutput = net(testingInput);
perf = perform(net,netTestingOutput,testingOutput)

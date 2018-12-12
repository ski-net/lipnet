import argparse
from trainer import Train

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--image_path', type=str, default='./data/datasets/')
    parser.add_argument('--align_path', type=str, default='./data/align/')
    parser.add_argument('--dr_rate', type=float, default=0.5)
    parser.add_argument('--use_gpu', type=bool, default=True)
    parser.add_argument('--num_workers', type=int, default=2)
    config = parser.parse_args()
    
    trainer = Train(config)
    
    trainer.train()

if __name__ =="__main__":
    main()
//
//  main.m
//  cocoaglass
//
//  Created by Shravan Reddy on 10/9/13.
//  Copyright (c) 2013 Moji, Inc. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "PXGlass.h"

int main(int argc, const char * argv[]) {

  
  @autoreleasepool {
    NSString *sketchPath = @"/Users/Simhadri/Desktop/Scratchpad/Preview Scripts/Test File.sketch";
    NSString *previewPath = [PXGlass exportPreview:sketchPath];
    
    NSLog(@"Preview path: %@", previewPath);
  }
  
  return 0;
}


//
//  main.m
//  QuickGlass
//
//  Created by Shravan Reddy on 10/28/13.
//  Copyright (c) 2013 Pixelapse. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "PXGlass.h"

int main(int argc, const char * argv[])
{

  //  QuickGlass -srcPath "/Users/Vayu/Desktop/Scratchpad/Preview Scripts/Test File.sketch" -destPath "/Users/Vayu/Desktop/outputfile.png" -exportFormat "png"
  @autoreleasepool {
      
    NSUserDefaults *args = [NSUserDefaults standardUserDefaults];
    
    // Required params
    NSString *srcPath = [args stringForKey:@"srcPath"];
    NSString *destPath = [args stringForKey:@"destPath"];
    
    // Optional
    float maxWidth = [args floatForKey:@"maxWidth"];
    float maxHeight = [args floatForKey:@"maxHeight"];
    NSString *exportFormat = [args stringForKey:@"exportFormat"];
    
    NSLog(@"srcPath: %@ destPath: %@ maxWidth: %f maxHeight: %f exportFormat: %@", srcPath, destPath, maxWidth, maxHeight, exportFormat);
    NSString *previewPath = [PXGlass exportPreview:srcPath destPath:destPath maxWidth:maxWidth maxHeight:maxHeight inFormat:exportFormat];
    
    NSLog(@"Preview path: %@", previewPath);

      
  }
    return 0;
}


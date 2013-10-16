//
//  PXGlass.m
//  cocoaglass
//
//  Created by Simhadri on 10/15/13.
//  Copyright (c) 2013 Moji, Inc. All rights reserved.
//

#import "PXGlass.h"
#import <QuickLook/QuickLook.h>

@implementation PXGlass

//////////////////////////////////////////////////////////////////////////
// FORMAT VALIDATION
//////////////////////////////////////////////////////////////////////////

+(bool)isValidFormat:(NSString*)format {
  // Error checking
  NSArray *supportedFormats = [NSArray arrayWithObjects: @"png", @"jpg", @"jpeg", @"tif", @"tiff", nil];
  
  if ([format length] == 0) {
		NSLog(@"Exception: No export format specified");
		return NO;
	}
  
  format = [format lowercaseString];
  if (![supportedFormats containsObject:format]) {
    NSLog(@"Exception: Unsupported export format");
		return NO;
	}
  
  return YES;
}

+(CFStringRef)stringToUTType:(NSString*)format {
  assert([PXGlass isValidFormat:format]);

  format = [format lowercaseString];

  if ([format isEqualToString:@"png"]) {
    return kUTTypePNG;
  }
  
  if ([format isEqualToString:@"jpeg"] || [format isEqualToString:@"jpg"]) {
    return kUTTypeJPEG;
  }
  
  if ([format isEqualToString:@"tiff"] || [format isEqualToString:@"tif"]) {
    return kUTTypeTIFF;
  }
  
  return NULL;
}

//////////////////////////////////////////////////////////////////////////
// SIZE VALIDATION
//////////////////////////////////////////////////////////////////////////

+(bool)isValidSizeWithWidth:(float)width withHeight:(float)height {
  if((width == 0.0) || (height == 0.0)) {
    return NO;
  }
  return YES;
}

//////////////////////////////////////////////////////////////////////////
// IMAGE EXPORT
//////////////////////////////////////////////////////////////////////////

+(NSString*)exportPreview:(NSString*)srcPath {
  return [PXGlass exportPreview:srcPath maxWidth:2640 maxHeight:1520];
}

+(NSString*)exportPreview:(NSString*)srcPath maxWidth:(float)width maxHeight:(float)height {
  return [PXGlass exportPreview:srcPath maxWidth:width maxHeight:height inFormat:@"png"];
}

// height, width - appropriate export size. Scale will be maintained
// format - optional params
// returns NSString - path to the written file
// returns nil if unable to generate preview
+(NSString*)exportPreview:(NSString*)srcPath maxWidth:(float)width maxHeight:(float)height inFormat:(NSString*)format {
  
  // Sanity checks
  assert([PXGlass isValidFormat:format]);
  assert([PXGlass isValidSizeWithWidth:width withHeight:height]);
  
  // Generate image preview
  CFURLRef srcURL = (__bridge CFURLRef)[NSURL fileURLWithPath:srcPath];
  CGSize maxPreviewSize = CGSizeMake(width, height);
  CFDictionaryRef exportOptions = (__bridge CFDictionaryRef)[NSDictionary dictionaryWithObjectsAndKeys:
                                                             [NSNumber numberWithBool:NO], (NSString*)kQLThumbnailOptionIconModeKey,
                                                             [NSNumber numberWithFloat:1.0], (NSString*)kQLThumbnailOptionScaleFactorKey,
                                                             nil];
  
  CGImageRef previewRef = QLThumbnailImageCreate(kCFAllocatorDefault, srcURL, maxPreviewSize, exportOptions);
  
  if (previewRef == NULL) {
    NSLog(@"Exception: Unable to export preview");
    return nil;
  }
  
  // Write preview out to file
  NSString *destPath = @"/Users/Simhadri/Desktop/outputfile.png";
  CFURLRef destURL = (__bridge CFURLRef)[NSURL fileURLWithPath:destPath];
  CFStringRef exportType = [PXGlass stringToUTType:format];
  CGImageDestinationRef destRef = CGImageDestinationCreateWithURL(destURL, exportType, 1, NULL);
  CGImageDestinationAddImage(destRef, previewRef, nil);
  
  if (!CGImageDestinationFinalize(destRef)) {
    NSLog(@"Exception: Failed to write image to %@", destPath);
    return nil;
  }
  
  CFRelease(destRef);
  CFRelease(previewRef);
  
  return destPath;
}
@end

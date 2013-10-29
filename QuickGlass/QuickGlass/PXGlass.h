//
//  PXGlass.h
//  QuickGlass
//
//  Created by Simhadri on 10/15/13.
//  Copyright (c) 2013 Moji, Inc. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface PXGlass : NSObject

+(NSString*)exportPreview:(NSString*)srcPath destPath:(NSString*)destPath;
+(NSString*)exportPreview:(NSString*)srcPath destPath:(NSString*)destPath maxWidth:(float)width maxHeight:(float)height;
+(NSString*)exportPreview:(NSString*)srcPath destPath:(NSString*)destPath maxWidth:(float)width maxHeight:(float)height inFormat:(NSString*)format;

+(bool)isValidSizeWithWidth:(float)width withHeight:(float)height;

@end

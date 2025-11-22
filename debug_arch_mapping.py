from mergekit.architecture.json_definitions import NAME_TO_ARCH
import json

print("Architectures for Gemma3ForConditionalGeneration:")
if "Gemma3ForConditionalGeneration" in NAME_TO_ARCH:
    for arch in NAME_TO_ARCH["Gemma3ForConditionalGeneration"]:
        print(json.dumps(arch.model_dump(mode='json'), indent=2))
else:
    print("Not found")

print("\nArchitectures for Gemma3ForCausalLM:")
if "Gemma3ForCausalLM" in NAME_TO_ARCH:
    for arch in NAME_TO_ARCH["Gemma3ForCausalLM"]:
        print(json.dumps(arch.model_dump(mode='json'), indent=2))
else:
    print("Not found")
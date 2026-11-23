---
title: The extension statement from semistable reduction
decls:
  - GlobalTheory.zhGeo_of_semistableReduction
  - GlobalTheory.T.zarhinGeometric_of_semistableReduction
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The extension statement from semistable reduction

The framed models of [the section on normal projective models](/entry/models-nonempty-z-on-of-components/) and the full level models of [the section on full level models](/entry/top-amp-exists/) use one input on theta systems, which we called *the geometric statement on theta systems*. The chapter on theta level structures along arcs calls it the [extension statement](/entry/zh-geo/): an abelian scheme with a theta structure over an open part $U_0$ of a model extends to a semi-abelian scheme over the whole model, with a cubical line bundle and theta sections that immerse it in projective space. That chapter proves the extension statement from a list of inputs. This section shows that all inputs but one are proved, so that the extension statement follows from the semistable reduction theorem alone. The background is [semi-abelian degenerations and Mumford's construction](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction).

We recall the statement of the input.

**Theorem 5.13.1 (Semistable reduction).** Let $p$ be a prime, $K$ a finite extension of $\mathbb{Q}_p$ in an algebraic closure, and $A$ a polarized abelian variety over $K$. Then there are a finite extension $K' \supseteq K$ and a semi-abelian group scheme $G$ over the ring of integers $\mathcal{O}_{K'}$ whose generic fibre is $A \times_K K'$ as a group scheme (A. Grothendieck, SGA 7 I, Exposé IX, Théorème 3.6).

Lean: `GlobalTheory.Published.SemistableReductionSt`.

This is the form stated in [the section on normal projective models](/entry/models-nonempty-z-on-of-components/). Grothendieck's theorem holds for every abelian variety over the fraction field of a discrete valuation ring; the form here is the special case of a polarized abelian variety over a $p$-adic field.

The extension statement is the following, in the words of [the chapter on theta level structures](/entry/zh-geo/). Let $o \subset \Omega$ be an arithmetic base, $S$ a big theta system with a realization $\rho$ by an abelian scheme, $M$ a model of the field $\Omega$ over $o$ with an admissible open set $U_0$, and $E$ a lattice system fixed by tests. Assume that there are vectors $G_1, \dots, G_n$ and an integer $a$ such that at every point, the local span of the $G_k$, divided by a power of a theta value, is the dual of the lattice of $E$. Then $\rho$ has an *extension*: a semi-abelian scheme $G$ over the model, of relative dimension $g$, with a map from the abelian scheme over $U_0$, a rigidified symmetric cubical line bundle, extensions of endomorphisms and of isomorphisms of line bundles, the abelian locus equal to the set where the torus part of the test vanishes, extended torsion sections, uniformizations over complete local domains, and theta sections that immerse $G$ into projective space locally over the model.

Lean: `GlobalTheory.ZH.ZHGeoSt`, `GlobalTheory.ZH.ZHOut`.

**Theorem 5.13.2 (The extension statement from semistable reduction).** If the semistable reduction theorem holds, then the extension statement holds.

Lean: `GlobalTheory.zhGeo_of_semistableReduction` (also `GlobalTheory.T.zarhinGeometric_of_semistableReduction`, a second name).

*Proof.* [The extension theorem for theta level abelian schemes](/entry/semi-abelian-scheme-uniformisation-exists-geometric/) proves the extension statement from the following inputs:

1. the homomorphism extension theorem: every homomorphism between the generic fibres of two semi-abelian schemes over a [[discrete valuation ring|MGM3CNJW9V]] extends uniquely;
2. the semistable reduction theorem;
3. the uniformization statement for degenerations: a semi-abelian scheme over a complete discrete valuation ring of characteristic $0$, whose closed fibre is an extension of an abelian variety by a split torus and whose generic fibre is polarized and satisfies a symmetry hypothesis, is uniformized by degeneration data;
4. the first five bundles of laws of abelian schemes;
5. the torsion statement for uniformizations: the torsion points of the generic fibre are described by the degeneration data, compatibly with the Weil pairing.

Inputs 1, 3, 4 and 5 are proved in other chapters: the homomorphism extension theorem over discrete valuation rings, the six bundles of laws (of which we keep the first five), and the uniformization and torsion statements, which are proved together. Input 2 is the hypothesis. So the extension theorem applies and gives the extension statement. $\square$

**Remark 5.13.3.** The theorem does not remove the hypothesis. The semistable reduction theorem is proved in its own chapter, and the corollaries of [the section on full level models](/entry/top-amp-exists-of-semistable-reduction/) and of [the section on local model systems](/entry/models-st-of-semistable-reduction/) keep it as a hypothesis. This theorem collects in one place the other inputs of the extension statement, so that those corollaries can cite one result. The uniformization and torsion statements are the shape of the theory of degeneration data of Mumford and of Faltings and Chai; we did not compare their Lean form with the book.

**Remark 5.13.4 (Formalization).** The proof is one `exact` after `obtain ⟨L, L2, L3, L4, L5, -⟩ := GlobalTheory.allSixLaws`, which discards the sixth bundle of laws ([ZarhinGeometricOfSemistableReduction.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ZarhinGeometricOfSemistableReduction.lean#L21)). The inputs are `GlobalTheory.homExtension_semiAbelian_dvr` for the homomorphism extension theorem, and the two parts of `GlobalTheory.ZH.thmU_and_uTors` for the statements `ThmUSt` and `UTorsSt`; they are passed to `T.semiAbelianScheme_uniformisation_exists_geometric`. The names of the theorem and of its file say "Zarhin" and `ZHGeoSt` has the letters "ZH", but the statement does not mention Zarhin's trick or any construction tied to Zarhin; it is the extension statement for theta systems. The semistable reduction statement is also proved in the Lean code, as `GlobalTheory.SS.semistableReductionSt`. The second name is a wrapper proved by `first | exact @...`.

---
id: hodge-iso-natural-cech
title: The graded pieces of the thickening cohomology are Hodge cohomology, naturally
kind: theorem
decl: CrystallineSemistableComparison.Om.Nt2F.hodge_iso_natural_cech
module: Development.WeilBound.CoreStatements.PadicHodgeComparison.EtaleCohomologyComparison.DifferentialFormsCech.CoverRefinementHodge.FinalC
covers: 380
status: drafted
drafted_by: writer@claude
---
This theorem identifies the groups $\mathrm{Hdg}(a, a+j)$, where the Hodge-Tate pairing takes its values, with the Hodge cohomology $H^j(X, \Omega^a)$ of a smooth proper variety, naturally in the variety. It is step 2 of the proof of [Hodge-Tate period matrices for smooth projective models](/entry/ht-spec-good/), which turns the pairing into an invertible period matrix. Below this theorem are 380 declarations.

## Statement

Let $K$ be a field and $X$ a scheme over $K$. The site `Thick` of $X$ has as objects the thickenings of opens of $X$ over $K$, with the zero ideal and the trivial divided powers on the base (`smFun`). On its structure sheaf there is the divided power filtration $J^{[r]}$. Put
$$\mathrm{Hdg}(a, n) = H^n\bigl(\mathrm{Thick}(X/K),\ J^{[a]} / J^{[a+1]}\bigr),$$
a $K$-module (`HT.Hdg`). We have not unfolded the site further. Let $\Omega^a$ be the sheafification of the presheaf of $a$-forms over $K$, and $H^j(X, \Omega^a)$ its sheaf cohomology (`HodgeC`, which is `hodgeH`). Both are contravariant in maps over $K$.

**Theorem.** Let $K$ have characteristic $0$. There are $K$-linear isomorphisms
$$e_X \colon \mathrm{Hdg}(a, a+j) \xrightarrow{\ \sim\ } H^j(X, \Omega^a)$$
for all $X$ smooth and proper over $K$ and all $a, j \geq 0$, such that $e_X(u^* x) = u^* e_Y(x)$ for each map $u \colon X \to Y$ over $K$ between such schemes.

## Proof

Fix for each $X$ a cover $\mathcal{U} = $ `covX q`: finitely many opens with étale coordinates, all of whose finite intersections are affine (`Pb.Cov`). The isomorphism `isoI` for $\mathcal{U}$ is a composite of three maps.

1. `glob_iso`: $\mathrm{Hdg}(a, a+j)$ is the $j$-th cohomology of the Čech complex of $a$-forms on $\mathcal{U}$ (`formCos`), naturally for maps of covers.
2. `formToCO`: that complex computes the Čech cohomology $\check H^j(\mathcal{U}, \Omega^a)$. It is bijective because the intersections are affine (`forms_to_cech_bijective`), and $K$-linear.
3. `cechOmAdd`: for a cover with affine intersections, $\check H^j(\mathcal{U}, \Omega^a) = H^j(X, \Omega^a)$. It is $K$-linear by `cech_forms_add_smul`.

`isoI_nat` proves the naturality $e_{\mathcal{U}}(u^* x) = u^* e_{\mathcal{W}}(x)$ when each open of the cover $\mathcal{U}$ of $X$ maps into an open of the cover $\mathcal{W}$ of $Y$. It uses the naturality clause of `glob_iso`, and `formCoch_pull` and `cechOm_pull` for steps 2 and 3. The fixed covers of $X$ and $Y$ need not satisfy this. So `cov_refine` gives a cover $\mathcal{U}'$ of $X$ that refines all the sets $\mathcal{U}_\alpha \cap u^{-1}\mathcal{W}_\beta$. Then `isoI_nat` for $u = \mathrm{id}$, with `pullH_id` and `pullC_id`, shows that $\mathcal{U}'$ and $\mathcal{U}$ give the same isomorphism. `isoI_nat` for $u$ and $\mathcal{U}'$ then gives the naturality.

## In the Lean code

The theorem is in [FinalC.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/DifferentialFormsCech/CoverRefinementHodge/FinalC.lean#L14). It applies `hdg_iso_of_ing` in [FormToCOBijectiveI.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/DifferentialFormsCech/CoverRefinementHodge/FormToCOBijectiveI.lean#L103) to nine proved inputs. The lemmas:

- `glob_iso` in [HodgeCechComparison.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/DifferentialFormsCech/GlobalDifferentialForms/HodgeCechComparison.lean#L47);
- `isoI` and `isoI_nat` in FormToCOBijectiveI.lean, lines 42 and 50;
- `CovRefine`, `PullHId`, `PullCId` in [CovRefine.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/DifferentialFormsCech/CoverRefinementHodge/CovRefine.lean#L14), proved in NeedPf.lean.

The statement is written `type_of% (@Om.hdg_iso _)`. Here `hdg_iso` in [HdgAffIso.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/DifferentialFormsCech/HdgAffIso.lean#L13) is the identity $P \to P$, so the statement is its hypothesis $P$. The same $P$ is written out again as `HdgIso` in [SpecOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/SpecOf.lean#L16), the form in which `htSpecGood_of` uses it. The isomorphism depends on the cover chosen by `Classical.choice`. The theorem shows that the choice does not matter for naturality.

---
id: kato-two-w-of-prints-h-of-r-t-of-quad-bc2
title: Vanishing of two Bloch-Kato Selmer groups, given the row and quadratic base change
kind: theorem
decl: UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH_of_rT_of_quadBC2
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.KatoTwoWOfPublishedH
covers: 9554
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement $\mathrm{KatoTwoW}$ from the extended hypotheses, the row statement $\mathrm{RowT}$ and quadratic base change $\mathrm{QuadBC2}$. [The theorem above it](/entry/kato-two-w-of-prints-h/) supplies the last two inputs, for the first count of the chapter [The window bound VWin](/proof/vwin/). The proof turns the condition $\mathrm{WitAQ}$ into a condition on Satake parameters, and then calls [the spherical form](/entry/two-s/) of the statement.

## Statement

**Theorem.** Assume $\mathrm{HypothesesH'}$, $\mathrm{RowT}$ and $\mathrm{QuadBC2}$. Let $\ell$ be a prime, $K$ a number field, $e, N$ integers, $\theta, \psi$ characters of $G_\mathbb{Q}$ and $W \colon G_\mathbb{Q} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ a [[Galois representation|JQEYEQJY2G]]. Suppose that the conditions $\mathrm{Used}$ hold:

1. on the numbers: $\ell$ is odd, $e \ge 1$, $\ell - 1 \nmid 2e$, $N \ge 1$ is even and prime to the discriminant $d_K$;
2. on $K$: it is imaginary quadratic and $\ell \nmid |d_K|\, h_K$;
3. on the characters: $\theta$ has kernel $G_K$ and $\theta^2 = 1$; $\psi$ is trivial on $\mu_N$, has order prime to $\ell$, and is quadratic on inertia above $\ell$; $\bar\chi^e\psi(c) = 1$ for a complex conjugation $c$;
4. on $W$: it meets a level condition for $N|d_K|$ with weights $(e, -e)$ and an ordinarity condition `OrdPoly` (we have not unfolded either); $\det W = \theta$; on inertia above $\ell$ its trace is $\bar\chi^e\psi + (\bar\chi^e\psi)^{-1}$; its trace is congruent to $\theta\,\bar\chi^e\psi + (\bar\chi^e\psi)^{-1}$ modulo the maximal ideal; it has a flag at $\ell$ with characters $\bar\chi^{e}\chi$ and $\bar\chi^{-e}\chi$ on inertia; and its restriction to $G_K \cap \ker \bar\chi$ is irreducible.

Here $\bar\chi$ is the [[cyclotomic character|XSGB5K2KEG]]. Let $f$ be a newform of weight $2e+1$ attached to $W \otimes \bar\chi^{-e}$, and suppose that $W$ satisfies $\mathrm{WitAQ}$. Then the Bloch-Kato Selmer groups of $W$ and of $W \otimes \theta$ vanish.

The Selmer group here is the group of cocycles unramified away from $\ell$ and in a finite part above $\ell$ (not unfolded), modulo coboundaries. $\mathrm{WitAQ}$ says: for every CM quadratic extension over which $W$ stays irreducible, the restriction of $W$ satisfies a local-global condition $\mathrm{WitA}$ on potentially unramified places and on the automorphic forms attached to it.

## Proof

1. From the hypotheses, $\mathrm{RowT}$ and $\mathrm{QuadBC2}$, `locQ_of_alt` proves a local statement $\mathrm{LocQ}$. We have not unfolded it.
2. From $\mathrm{Used}$ and $f$, `Used.adm` proves that $\det W = \theta$ and that $W$ is admitted.
3. Apply [`twoS`](/entry/two-s/). Its inputs are the Galois cohomology field `litN.coh` and a source statement $\mathrm{SrcS}$ made by `srcS_alt` from `twNew_alt` and `frobRoot_alt`. It remains to prove that $W$ has Satake parameters at the places above $\ell$, in the sense of $\mathrm{SphAt}$.
4. Apply `sphOfWit`, made from `twWit_alt` and $\mathrm{LocQ}$. It turns $\mathrm{WitAQ}$ into $\mathrm{SphAt}$ for a continuous irreducible $W$ whose determinant is trivial on $G_{\mathbb{Q}(\mu_M)}$ for some $M \ge 1$.
5. The kernel of $\det W$ is open and contains the commutator subgroup. By the Kronecker-Weber theorem (Washington, *Introduction to Cyclotomic Fields*, Theorem 14.1) it contains $G_{\mathbb{Q}(\mu_M)}$ for some $M \ge 1$. In Lean this is `UpperTheory.V.CF.kwAbs`.

## In the Lean code

The theorem is in [KatoTwoWOfPublishedH.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/KatoTwoWOfPublishedH.lean#L38). $\mathrm{KatoTwoW}$ is in [KatoTwoW.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SphericalDecomposition/KatoTwoW.lean#L10) and $\mathrm{Used}$ in [KatoTwoOfUseN.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/KatoTwoOfUseN.lean#L11).

- `locQ_of_alt`, in the same file at line 35.
- `sphOfWit`, `twWit_alt`, `aIsoTwOf_alt`, and $\mathrm{SphOfWit}$ in [SphOfWit.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SphericalDecomposition/SphOfWit.lean#L79).
- `UpperTheory.V.CF.kwAbs`, in [KwAbs.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/ClassFieldRamification/KwAbs.lean#L7).

The fact $\det W = \theta$ from step 2 is not used. The hypothesis $\mathrm{QuadBC2}$ is a theorem (`quadBC2`), so it is not a real assumption. $\mathrm{RowT}$ is used only through $\mathrm{LocQ}$.

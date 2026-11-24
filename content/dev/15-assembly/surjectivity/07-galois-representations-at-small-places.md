---
title: Galois representations at small places
decls:
  - GlobalTheory.FrameGal.galois_steinberg_local_alt
  - GlobalTheory.T.galois_frame_compatibility_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Galois representations at small places

This section attaches Galois representations to the eigensystems of a frame at a small place. For each eigensystem $\theta$ there is a crystalline representation of the absolute Galois group of the host field $E$ in $\mathrm{GL}_{N_r}(\overline{\mathbb{Q}}_\ell)$ whose Frobenius polynomials at the block places are read off $\theta$. If $\theta$ lies in the block, the representation splits off $t$ crystalline characters. The proof takes the automorphic system of Section 6, transfers it to $\mathrm{GL}_{N_r}$ by base change, and applies the construction of Galois representations for polarized cusp forms. This is where most published inputs of the exponent bound enter. [The model statement of Section 8](/entry/model-st-of-small-frame-gal/) uses the result. The background is in [the Galois representation of an automorphic representation](/learn/galois-representations/#the-galois-representation-of-an-automorphic-representation) and in [crystalline representations](/learn/galois-representations/#crystalline-de-rham-and-potentially-semistable-representations).

We first state the published inputs of this section. Let $E$ be a CM field with maximal real subfield $E^+$, and $\Omega$ an algebraic closure of $E$. Write $G_E = \mathrm{Gal}(\Omega / E)$.

**Theorem 5.7.1 (Regular algebraic cusp forms are cohomological).** Let $E$ be a totally complex number field and $a \ge 1$. Each cuspidal automorphic representation of $\mathrm{GL}_a(\mathbb{A}_E)$ that is regular algebraic is cohomological.

Lean: `GlobalTheory.Published.ClozelCohomological`.

This is a lemma of Clozel (*Motifs et formes automorphes*, 1990, Lemma 3.14).

**Theorem 5.7.2 (Galois representations of polarized cusp forms).** Let $\ell$ be a prime, $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$ an isomorphism and $a \ge 1$. Let $\pi$ be a regular algebraic cuspidal automorphic representation of $\mathrm{GL}_a(\mathbb{A}_E)$ that is polarized by a Hecke character $\chi$ of $E^+$. Then there are a representation $r \colon G_E \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$, a weight and Hodge-Tate multisets at the embeddings of $E$ such that $r$ is attached to $\pi$, $\chi$ and $\iota$ in the sense of local-global compatibility at the unramified places, with the given Hodge-Tate weights.

Lean: `UpperTheory.GalS.CuspUAlt`.

This is the theorem of Chenevier and Harris (2013), which completes the work of Shin (2011) and of Harris and Taylor (2001).

**Theorem 5.7.3 ($\ell$-adic characters of Hecke characters).** For each number field $E$ there is a global Artin map, and each algebraic Hecke character of $E$ has an attached continuous $\ell$-adic character of $G_E$ that agrees with it at the unramified places; a second form gives the same with control of the places above $\ell$.

Lean: `GlobalTheory.Published.HeckeLAdicCharacter` (also `GlobalTheory.Published.HeckeLAdicCharacterAbove`, the form at the places above $\ell$).

This is due to Weil and is treated in Serre, *Abelian $\ell$-adic Representations and Elliptic Curves*, Chapter II.

**Theorem 5.7.4 (Base change for definite unitary groups).** An automorphic representation of a definite unitary group over $E^+$, split by $E$, has a base change to an isobaric automorphic representation of $\mathrm{GL}_N(\mathbb{A}_E)$, compatible with the local base change at the split and unramified places.

Lean: `GlobalTheory.Published.BaseChangeDefiniteUnitaryGroup`.

This is a theorem of Labesse (*Changement de base CM et séries discrètes*, 2011).

**Theorem 5.7.5 (Local Langlands correspondence).** For each finite extension $K$ of $\mathbb{Q}_p$ and each $n$ there is a bijection between the smooth irreducible representations of $\mathrm{GL}_n(K)$ and the Frobenius semisimple $n$-dimensional Weil-Deligne representations of $K$ with the usual compatibilities.

Lean: `UpperTheory.Zero.LLC.RecTExists`.

This is the theorem of Harris and Taylor (2001) and of Henniart (2000). In the proof of Section 1 it is built from the local hypotheses as in [the step on it](/step/rect-exists-def/).

Now the conclusion. Keep the notation of Sections 5 and 6, and write $h_0$ for the weight constant of $P$.

**Definition 5.7.6 (Galois side).** Let $F$ be a frame of rank $N_r$ at $\ell$, with embeddings $\mathrm{inc}_\tau$ of $E$ into $\overline{\mathbb{Q}}_\ell$. The *Galois side* holds for $F$ if there are a set of places, a choice of indices $\mathrm{pt}$, a Frobenius datum and a map $\epsilon$ on embeddings, equal to the identity or to complex conjugation, with two properties.

1. For each eigensystem $\theta$ for weights $\mu$ with antitone residues, there are a representation $r \colon G_E \to \mathrm{GL}_{N_r}(\overline{\mathbb{Q}}_\ell)$ and jumps $J$ at the embeddings, given by $\mu$ at $\epsilon \circ \mathrm{inc}_\tau$ and by $h_0$ minus the reversed values at the conjugate, such that $r$ is crystalline with Hodge-Tate weights $J$, and the characteristic polynomials of $r$ at the Frobenius elements are read off $\theta$.
2. For each eigensystem $\theta$ for the weights $\lambda$ of $W$ that lies in the block, there are $a$ with $a + t = N_r$, a continuous representation $\rho \colon G_E \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$, characters $\chi_0, \dots, \chi_{t-1}$ of $G_E$ and a bottom weight $b$, such that each $\chi_s$ is crystalline with Hodge-Tate weight $b + s$, the values of $b$ at $\epsilon \circ \mathrm{inc}_\tau$ and its conjugate are fixed by $W$, and at the Frobenius elements

$$\begin{aligned} \operatorname{charpoly}(\sigma) = \operatorname{charpoly}\big(\rho(\sigma)\big) \cdot \prod_{s < t} \big(X - \chi_s(\sigma)\big). \end{aligned}$$

Here "read off $\theta$" means: at a place $Q$ with Frobenius $\sigma$ and sign $\pm 1$, the reverse of the characteristic polynomial at $\sigma^{\pm 1}$ is the Hecke polynomial of degree $N_r$ at the norm of $Q$ with coefficients $\theta_{\mathrm{pt}(Q, k)}$, twisted by a fixed character.

Lean: `GlobalTheory.ExpFrame.GalSide`.

**Definition 5.7.7 (Galois statement).** The *Galois condition* at $w$ holds if the Galois side holds for each good frame of rank $N_r$ at $\ell$ with a reading of the block and a tie. The *Galois statement* is the Galois condition, in range.

Lean: `GlobalTheory.ExpTie.GalAt` (also `GlobalTheory.ExpTie.GaloisStatement`).

**Theorem 5.7.8 (Galois representations at small places).** Assume that regular algebraic cusp forms are cohomological, the two theorems on $\ell$-adic characters of Hecke characters, the Chebotarev density theorem in degree one, the theorem on Galois representations of polarized cusp forms, base change for definite unitary groups, the theorem of Bhatt and Scholze on crystalline lattices, and the local Langlands correspondence. Then the smallness condition implies the Galois statement.

Lean: `GlobalTheory.FrameGal.galois_steinberg_local_alt` (also `GlobalTheory.T.galois_frame_compatibility_alt`, a second name).

*Proof.* By Section 6 the smallness condition gives the automorphy statement. So, in range, the automorphy condition holds at each small $w$. Fix such $w$, a good frame $F$ with a reading $R$, embeddings $\mathrm{inc}$ and a tie $T$. Take the places of the block that are prime to $\ell$, and for each such $Q$ and each $k < N_r$ the index $\mathrm{pt}(Q, k)$ with Hecke index $k + 1$ at $Q$; the tie gives it. The block numbers give $n$, $t$ and the block values $\nu$.

The theorem on compatible systems now gives the Galois side from the following data: the eight published inputs; the fact that the host field is unramified at the places that matter; the isomorphism $\iota$, the half system and the shifts of $T$; the numerical checks; the finite set of places; the places of the block, which are split and prime to $\ell$; and two facts that we check.

1. For each eigensystem $\theta$ for weights $\mu$, the automorphy condition gives an automorphic system $\pi$. At each block place $Q$ prime to $\ell$, the Satake parameter $S$ of $\pi$ at $\lambda_Q$ satisfies: the $k$-th elementary symmetric function of $S$, normalized, is $\iota(\theta_{\mathrm{pt}(Q, k)})$ for $1 \le k \le N_r$, and the value at $k = 0$ is $1$. So the Hecke polynomial of $\pi$ at $\lambda_Q$ has the coefficients of $\theta$.
2. For each eigensystem $\theta$ in the block and each block place $Q$, the value $e_0(\nu(Q))$ is a root of the Hecke polynomial of $\theta$ at $Q$ of the right absolute value: its square norm is $q_Q^{\,n - t}$ by the good places, and the block divisibility gives the linear factor.

Base change takes $\pi$ to $\mathrm{GL}_{N_r}$; the result is cohomological by Clozel, and the Galois representation of the polarized parts gives $r$ with the Frobenius polynomials of fact 1. Its crystallinity at $\ell$ comes from the unramified places above $\ell$ and the crystalline lattices. In the block, fact 2 splits off the characters $\chi_s$, which come from Hecke characters by the $\ell$-adic characters, with Chebotarev to fix them by their Frobenius values. $\square$

**Remark 5.7.9 (Formalization).** The theorem is in [GaloisAtPlaceOfAutomorphicAtPlace.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GaloisAtPlaceOfAutomorphicAtPlace.lean#L154), and the pointwise step at line 120. The second name at line 168 is a one-line call with `maxHeartbeats` set to 1000000. The name "Steinberg local" has nothing to do with the statement: no Steinberg representation occurs. The Galois side is in [HasBlockOfOccurs.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasBlockOfOccurs.lean#L244). The theorem on compatible systems, which takes all eight inputs and does the work of the last paragraph of the proof, is not opened here; the last paragraph is our reading of the role of each input, not a check of the Lean proof. Six of the eight inputs (all but Chebotarev and Bhatt-Scholze) are used only through this theorem. We have not unfolded the published inputs; the statements above are their published forms, matched to the Lean names, and we have checked the Lean types only for the first two. The Lean name of the base change input is an abbreviation of a statement on definite unitary groups that we have not opened.

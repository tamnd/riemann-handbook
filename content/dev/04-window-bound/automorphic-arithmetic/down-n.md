---
id: down-n
title: Descent of a normalised conjugation-invariant cusp form to the rationals by a theta lift
kind: theorem
decl: UpperTheory.ConvolutionTheory.RankTwoDescent.downN
module: Development.AutomorphicArithmetic.Foundations.Convolution.SplitEigenfunctions.UnitOfNormalised
covers: 1501
status: drafted
drafted_by: writer@claude
---
This theorem does the main work of [the descent from an imaginary quadratic field](/entry/desc-s/). It takes a normalised [[cuspidal representation|9AZ164C298]] of $\mathrm{GL}_2$ over $E$ that is invariant under conjugation, and it finds a cuspidal representation over $\mathbb{Q}$ with the same Satake parameters at the split primes. The proof uses a [[theta correspondence|ZBGT50BW0Z]] between $\mathrm{GL}_2$ over $\mathbb{Q}$ and $\mathrm{GL}_2$ over $E$.

## Statement

Let $E$ be a totally complex number field with $[E:\mathbb{Q}] = 2$. Let $P$ be a cuspidal subspace of automorphic forms on $\mathrm{GL}_2$ over $E$. Suppose that $P$ is normalised: $\varphi(z g) = \varphi(g)$ for $\varphi \in P$ and $z$ in the split part of the centre (`IsNormalised`). Suppose also that $P$ is conjugation invariant: for cofinitely many primes $w$, each prime $w'$ over the same rational prime has a common Satake parameter with $w$ (`ConjInv`).

**Theorem.** There is a cuspidal representation $\pi'$ of $\mathrm{GL}_2$ over $\mathbb{Q}$ such that its Satake parameters at $w \cap \mathbb{Z}$ are those of $P$ at $w$, for cofinitely many $w$ with $Nw = N(w \cap \mathbb{Z})$ (`SplitBC`). Each infinitesimal character of $P$ at $\tau$ is also an infinitesimal character of $\pi'$ at $\tau$ restricted to $\mathbb{Q}$.

## Proof

1. `datEx` gives a datum `Dat`: an element $\delta \in \mathbb{Q}$ that is negative at the real place, an element $\theta \in E$ with $\theta^2 = \delta$ and the conjugation $\sigma$. With it, the space $V_4 = \mathbb{Q}^4$ is identified with the $2 \times 2$ Hermitian matrices over $E$, and $h \in \mathrm{GL}_2$ acts by $X \mapsto h X \bar{h}^{T}$.
2. `weilEx` gives a Weil representation `Weil` of $\mathrm{SL}_2(\mathbb{A}_\mathbb{Q})$ and of $\mathrm{GL}_2(\mathbb{A}_E)$ on Schwartz-Bruhat functions on $V_4$, with a quadratic character $\eta$ of $E/\mathbb{Q}$.
3. `measEx`, `measEEx` and `uMeasEx_of` give the measures.
4. `cenEx_of` gives a Hecke character $\omega$ of $\mathbb{Q}$ such that the central character of $P$ is $\omega \circ N_{E/\mathbb{Q}}$.
5. The private lemma `unit_of_normalised` shows $|\omega| = 1$. A normalised $P$ is unitary, and an idele $a$ of $\mathbb{Q}$, seen in $E$, has norm $a^2$. So $|\omega(a)|^2 = 1$.
6. `asaiNV` says that the periods of $P$ against $\omega^{-1}$ and against $(\omega\eta)^{-1}$ do not both vanish.
7. `perU_of` says that if all the periods `UPer` vanish, then both of these periods vanish. So some form $\varphi \in P$ and some $h$ have a nonzero `UPer`. This is an integral of $\varphi$ over $\mathrm{SL}_2(\mathbb{Q}) \backslash \mathrm{SL}_2(\mathbb{A}_\mathbb{Q})$ and then over the norm one ideles.
8. `rev_holds` turns this into a representation $\pi$ of $\mathrm{GL}_2$ over $\mathbb{Q}$ and the theta lift of a vector of $\pi$ and a Fock vector, which has a nonzero pairing with a form in $P$.
9. `toII` moves this to a nonzero pairing of the second kind, and `finS` reads off $\pi'$ with the matching parameters.

## In the Lean code

The theorem is at [line 32 of UnitOfNormalised.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/UnitOfNormalised.lean#L32), and `unit_of_normalised` is at [line 20](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/UnitOfNormalised.lean#L20). `DownN` is in [SplitEig.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/SplitEig.lean#L97), and `ConjInv`, `CenN` and `AsaiNV` are in [ConjInv.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/ConjInv.lean#L39). `Dat` is in [ThetaLiftTrivialOrbitTermsVanish.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/RealGroupAnalysis/ThetaLiftTrivialOrbitTermsVanish.lean#L134). `UPer`, `PerU`, `Rev` and `ToII` are in [ThetaLiftEqAnisotropicPart.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/ThetaLiftEqAnisotropicPart.lean#L160).

We have not unfolded the proofs of `asaiNV`, `rev_holds`, `toII` and `finS`. The quadratic space of Hermitian matrices and the use of the twists by $\omega^{-1}$ and $(\omega\eta)^{-1}$ suggest periods of Asai type, but we do not name a source for this exact argument.

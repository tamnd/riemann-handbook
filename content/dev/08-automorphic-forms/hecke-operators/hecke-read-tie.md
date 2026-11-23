---
id: hecke-read-tie
title: Geometric Hecke operators read as sums over cosets
kind: theorem
decl: GlobalTheory.HeckeReadProof.heckeReadTie
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.HeckeReadTie
covers: 340
status: drafted
drafted_by: writer@claude
---
This theorem proves `HeckeReadTie`, the third part of [the Hecke conjunction](/entry/hecke-int-transform-read-tie/). It says that a Hecke operator at a split prime, defined on sections by a sum over isogenies, becomes the adelic Hecke operator, a sum over coset translates, on the attached automorphic functions. Below it are 340 declarations. The term by term comparison is [`heckeTerm`](/entry/hecke-term/); this theorem sums it.

## Statement

Fix a datum $D$, a core $T$, real data $R$ and a face $F$ with the level, group, family, model, theta and tie conditions. Fix an index $i$, the base embedding $\sigma = \sigma_0$, and an identification of the space $V_{i+1}$ of $T$ at $\sigma$ with the hermitian space $W_i$. Let $G(\mathbb{A})$ be the adelic unitary group of $W_i$. The core gives each $h \in G(\mathbb{A})$ a framed point $y_h$ of the moduli space, and each section $f$ of weight $\kappa_i$ a function

$$\varphi_f(h) = \lambda \, c(h)\, \mu(h)\, f(y_h)$$

(`phiW`, in the form `phiW_eq`). We have not unfolded $\lambda$ (`lieFac`), $c$ or $\mu$.

Hecke data at a prime $\mathfrak{P}$ of $E$ are $p$, $k$, $\alpha \in G(\mathbb{A})$ and a finite set $R_c \subset G(\mathbb{A})$ with: $\mathfrak{P}$ split off, $p$ prime, $p \in \mathfrak{P}$, $p \nmid M'$, $k \le r$, $\alpha$ a Hecke element at $\mathfrak{P}$ of degree $k$, and $R_c$ a set of representatives for the double coset of $\alpha$ (`IsUnitaryHeckeOperatorSplitPrimeData`).

For a framed point $y$, let $\mathcal{C}(y)$ be the set of subgroups $C$ of the torsion of the abelian variety at $y$ that are $\mathcal{O}_E$-stable, isotropic for the Weil pairing, and of the order and type fixed by $\mathfrak{P}$ (`hkKer`, `HeckeKer`). Write $z \in y/C$ when an isogeny with kernel $C$ takes $y$ to $z$ and respects the frames (`hkRelFr`). Say $g = s\,T_{\mathfrak{P}} f$ if $g(y) = s \sum_{C \in \mathcal{C}(y)} f(z_C)$ at all points $y$ over algebraically closed fields, with $z_C$ a chosen point of $y/C$, or the term $0$ if there is none (`GeoHecke`, `hkVal`).

**Theorem.** Assume `SplitLinearModel D` and `VacFixed D` for all $D$. If the frame pin `FramePin` holds at $i$, then for all Hecke data, all $c_q$ and all sections $f, g$ of weight $\kappa_i$ with $g = c_q N(\mathfrak{P})^{-\lfloor k n_V/2 \rfloor} T_{\mathfrak{P}} f$, and all $h$:

$$\varphi_g(h) = \sigma(c_q)\, \mu_i(\mathfrak{P})^{-k} \sum_{a \in R_c} \varphi_f(ha).$$

Here $\mu_i(\mathfrak{P})$ is the value of the character `R.C.mu0 i` at $\mathfrak{P}$.

## Proof

Fix $h$. By `exists_witness`, $y_h$ is defined. By `phiW_eq`, $\varphi_g(h) = \lambda c(h)\mu(h) g(y_h)$. The relation $g = s T_{\mathfrak{P}} f$ at $y_h$ splits off $\sigma(c_q)$ and writes $g(y_h)$ as a sum over $C \in \mathcal{C}(y_h)$. [`heckeReading_kernels_match_cosets_through_frame`](/entry/hecke-reading-kernels-match-cosets-through-frame/) gives a bijection $e \colon \mathcal{C}(y_h) \to R_c$ and the term identity: the term at $C$, with the factor $\lambda c(h)\mu(h)N(\mathfrak{P})^{-\lfloor k n_V/2\rfloor}$, is $\mu_i(\mathfrak{P})^{-k}\varphi_f(h\, e(C))$. Reindexing the sum by $e$ gives the sum over $R_c$. The rest is bookkeeping.

## In the Lean code

The theorem is in [HeckeReadTie.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeReadTie.lean#L34). `HeckeReadTie` is in [HkSupSizedOfHkSup.lean](lean:Development/AbelianVarietyTheory/Statements/HeckeThetaIntegrals/HkSupSizedOfHkSup.lean#L22), and `ReadsAt`, `GeoHecke` and `phiW` are in [RealPoints.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/RealPoints.lean#L93). The lemmas:

- `phiW_eq`, in the same file, line 20.
- `exists_witness` in RealPoints.lean, line 73.
- `heckeReading_kernels_match_cosets_through_frame`, called with the proved point laws `HeckePointLaw.heckePointLaws` (HeckePointLaws.lean, line 10).

The two hypotheses are only passed down. The hypothesis that $g$ has weight $\kappa_i$ (`hg`, line 37) is never used. The exponent $k n_V / 2$ is a division of natural numbers, so it rounds down.

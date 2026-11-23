---
id: theorem-a-closing
title: The local colength bound for crystalline lattices
kind: theorem
decl: GlobalTheory.theoremA_closing
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LocalLiftingTheoremAOfBlochKatoTateDualityEulerC
covers: 1179
status: drafted
drafted_by: writer@claude
---
This theorem proves a bound on the cokernel of the map on Bloch-Kato [[Galois cohomology|9MPCZ3EAJM]] $H^1_f$ given by a surjection of crystalline lattices, at all odd primes $\ell$. It assumes three statements of local Galois cohomology. It proves the thirteen local inputs of the bound from them, and then calls the bound itself. Its only user is [its renaming](/entry/local-lifting-of-bloch-kato-tate-duality-euler-char/), which goes to [the twisted place bound](/entry/twisted-place-bound-closing/).

## Statement

Fix a prime $\ell \ne 2$. Let $K$ and $L$ be finite extensions of $\mathbb{Q}_\ell$ in $\overline{\mathbb{Q}}_\ell$, with ring of integers $\mathcal{O}$ of $L$. Let $K_0 = K \cap \mathbb{Q}_\ell^{\mathrm{ur}}$, $n = [K_0 : \mathbb{Q}_\ell]$ and $e = [K : K_0]$. The pair is *good* (`Good K 1 LL`) if $K \subseteq K_0(\mu_\ell)$ and each embedding of $K_0(\mu_\ell)$ into $\overline{\mathbb{Q}}_\ell$ has image in $L$.

The local part of the datum $D$ gives period rings $B$ and $B_{\mathrm{dR}}$ with their structure. For a $G_K$-stable $\mathcal{O}$-lattice $T$ in a continuous representation $V$ over $L$, the code defines $D_{\mathrm{cris}}(V)$, the filtered pieces of $D_{\mathrm{dR}}(V)$ at each embedding $\tau \colon K \to L$, and calls $V$ *crystalline* if $\dim_L D_{\mathrm{cris}}(V) = n \dim_L V$. An integer $a$ is a *jump* at $\tau$ if $\mathrm{Fil}^{a+1} \ne \mathrm{Fil}^a$, and $\mathrm{mult}_\tau(a) = \dim \mathrm{Fil}^a - \dim \mathrm{Fil}^{a+1}$.

A cocycle $c \colon G_K \to T$ is *finite* if $c(g) \otimes 1 = g x - x$ for some $x \in V \otimes B$. This is the definition of $H^1_f$ of Bloch and Kato (Grothendieck Festschrift I, 1990, Section 3), at the level of cocycles. For a $G_K$-map $f \colon T_1 \to T_2$, let $\operatorname{col}(f)$ be the $\mathcal{O}$-length of $Z^1_f(T_2)$ modulo the part that lies in $f(Z^1_f(T_1)) + B^1(T_2)$.

**Theorem.** Assume `BlochKatoLocal`, `LocalTateDualityK` and `LocalEulerCharK` (see [the renaming](/entry/local-lifting-of-bloch-kato-tate-duality-euler-char/)). Let $C \ge 160$. Let $\ell$, $K$, $L$ be good with $\ell \ne 2$. Let $f \colon T_1 \to T_2$ be a map of crystalline lattices that is onto on lattices, with $r = \dim V_2$. Let $S, \eta, m, h \in \mathbb{N}$, and for each $\tau$ let $b_\tau > \eta$ and a sign $\epsilon_\tau$. Suppose that for each $\tau$:

1. the jumps of $T_1$ lie in $[-h, h]$, and in $[-\eta, \eta] \cup \epsilon_\tau [b_\tau, b_\tau + S]$;
2. $\sum_{|a| \le \eta} \mathrm{mult}_\tau(T_2, a) \le m$;
3. $e = 2$, or $\epsilon_\tau$ depends only on $\tau|_{K_0}$.

Then $\operatorname{col}(f)$ is finite and $\operatorname{col}(f) \le \beta \cdot \operatorname{length}_{\mathcal{O}}(\mathcal{O}/\ell)$, where

$$\beta = C(ne+1)\,r\Big(\frac{eh}{\ell} + eS + e\log_\ell h + 1 + \eta\Big) + ne(e+1)\,m\,C(h+1).$$

The data $HW$ (Wach modules), $F$ and $Cm$ are quantified but do not occur in the conclusion.

## Proof

1. `GlobalTheory.T.localLifting_theoremA_hypotheses_admitted` proves `Adm1 D HW F Cm 23 32 32` from the three assumptions. `Adm1` is a conjunction of thirteen local facts. Among them: a bound on generators of $H^1_f$ (`adm7`); $\dim D_{\mathrm{cris}} \le n \dim V$ and $\dim D_{\mathrm{dR},\tau} \le \dim V$ (`adm8`); in a short exact sequence of lattices with crystalline middle term, the ends are crystalline and the multiplicities add (`adm11`); crystalline representations stay crystalline on restriction to a finite extension (`adm12`); naturality of Herr-type class maps of Wach modules; and a lifting statement with the constants $23, 32, 32$. The other conjuncts are not unfolded here.
2. [`integralityFromMetric_of_160_le`](/entry/integrality-from-metric-of-160-le/) says `Adm1 → Conclusion1 D C` for $C \ge 160$. It is applied with the same constants.

## In the Lean code

The theorem is at [LocalLiftingTheoremAOfBlochKatoTateDualityEulerC.lean line 14](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLiftingTheoremAOfBlochKatoTateDualityEulerC.lean#L14). The proof is two lines. The definitions are in [ElementDenominator.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ElementDenominator.lean#L36) (`thmA`, line 36; `Conclusion1`, line 54; `Adm1`, line 157) and in [Statement.lean](lean:Formalism/WeaklyAdmissibleFiltrations/Statement.lean#L262) (`LatHom.col`).

- The sign $\epsilon_\tau$ is the Boolean `up τ`, and $\epsilon_\tau[b, b+S]$ is the set `deep`.
- The three assumptions are used only to prove `Adm1`. `localLifting_theoremA_hypotheses_admitted` is a renaming of `AdmittedPartOne.all_admitted`, whose proof this page has not unfolded.
- The conclusion is named `TheoremBLocal`, although it is built from `thmA` and this theorem is called Theorem A.

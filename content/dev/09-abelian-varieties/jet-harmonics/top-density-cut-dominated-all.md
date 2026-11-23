---
id: top-density-cut-dominated-all
title: Domination of cut-off top densities, in the form for dominated convergence
kind: theorem
decl: GlobalTheory.HatNF.topDensity_cut_dominated_all
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.TopDensityCutoffDominatedOfHCXi
covers: 623
status: drafted
drafted_by: writer@claude
---
This theorem proves `NFTopDomAll` from `BesselXiIntegrable`. `NFTopDomAll` is the domination hypothesis of a dominated convergence argument (`limEvT_of_NF`), which lets the cutoff parameter $\varepsilon$ go to $0$ in the top densities. The theorem is a short reduction to [`top_density_dominated`](/entry/top-density-dominated/), which has the real content. Its restatement is [`T.topDensity_cutoff_dominated_of_HC_xi`](/entry/top-density-cutoff-dominated-of-hc-xi/).

## Statement

We use the notation of [A pointwise bound for discrete series coefficients](/entry/discrete-series-coef-pointwise-bound/) for $n = 2r+k+1$, the parameter $P$, the place datum $p$, the points $\mathrm{big}(c)$ and $G_p$. For a word $w$ (a list of letters $(b, y) \in \{\text{true}, \text{false}\} \times \mathbb{R}$) and a function $H$ on $n \times n$ matrices, let $E^w_H(\gamma)$ be the density `TBB.Ew p 1 H (r+1) w γ`; for the empty word it is the density $E_H$ of that entry. On matrices put $G(g) = |\Delta_{r+1}(g)|^2 - T_p |\Delta_r(g)|^2$, with $\Delta_j$ the minors `Dmin` built from the base data of $p$.

**Theorem.** Assume `BesselXiIntegrable`. For each $C_b$ there is $C_c$ with this property. Let $f$, $A_0 \in \mathbb{R}$, $p_0, N \in \mathbb{N}$ and $\chi \colon \mathbb{R} \to \mathbb{R}$ satisfy (`NFHyp`):

1. $\chi$ is smooth, vanishes on $(-\infty, \delta)$ for some $\delta > 0$, and is $1$ on $[1, \infty)$;
2. `InDDplus2` with constant $C_b$: each word operator $\Theta_{w,e}$ of $p$ agrees on a domain with a differential operator of the class `C6.InDDPlus` with indices $o \le C_b |w| n$ and $\kappa \le C_b (r+1) o$ (we have not unfolded this class);
3. $f$ is smooth on $G$, and for each $m$, $\|g\|^{A_0} |D f(g)|$ is bounded on $G$ for each product $D$ of at most $m$ unit Lie algebra derivatives (`InCC A₀ m f`);
4. $C_c (r+1)^4 (N n^2 + n^3) \le A_0 - (2r+2) p_0$;
5. $N \le 2 p_0$.

Let $Y \subset \mathbb{R}$ be finite and let $w$ be a word of length at most $N$ that is admissible for $Y$. Put $F_\varepsilon(g) = \chi(G(g)/\varepsilon)\, G(g)^{p_0} f(g)$. Then, for all small $\varepsilon > 0$, the map $c \mapsto E^w_{F_\varepsilon}(\mathrm{big}(c))$ on $\mathbb{C}^{r+1}$ is almost everywhere strongly measurable, and there is one integrable $h$ with $|E^w_{F_\varepsilon}(\mathrm{big}(c))| \le h(c)$ for almost all $c$ and all small $\varepsilon > 0$.

## Proof

Apply `top_density_dominated` with $a = 0$. Its input `BasicLiftAll 0` is `T.basicOperators_polynomialLift_no_inversePower`. Its hypothesis $N(1 + 2a(r)) \le 2p_0$ is item 5. Its word hypothesis `CutWord` is the first half of admissibility. A `simp` step identifies $F_\varepsilon$ (`D.cutF` of `fpm p f id p₀`) with the function `mulG` of `top_density_dominated`. That theorem holds for every $\varepsilon > 0$ and every $c$, which is more than the statement asks.

## In the Lean code

The theorem is at [TopDensityCutoffDominatedOfHCXi.lean line 11](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/TopDensityCutoffDominatedOfHCXi.lean#L11). `NFTopDomAll`, `NFHyp` and `NFTopDom` are in [CutLimENF.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutLimENF.lean#L48), and `IsCut0` is in [BigCellVanishingOfCommute.lean](lean:Formalism/HermitianCurvature/BigCellVanishingOfCommute.lean#L105).

The set $Y$ plays no role: the proof uses only the `CutWord` half of `AdmW`. `BesselXiIntegrable` is only passed along.

---
id: class-bound
title: A crystalline extension class lies in H^1_f up to a bounded power of ℓ
kind: theorem
decl: GlobalTheory.Cyc.ClassBound.class_bound
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CrystallineExtensionClassBound
covers: 619
status: drafted
drafted_by: writer@claude
---
This theorem proves `TBat`: the push-forward of the class of a crystalline extension to a twist $V_e/T_e$, times an explicit power of $\ell$, is a Bloch-Kato class. It is the proof of [the crystalline extension class bound](/entry/crystalline-extension-class-bound/), which goes into [the assembly](/entry/tb-assembled/). The proof joins two torsion results to [the lattice lemma](/entry/mem-hf-d-of-lattice/).

## Statement

Fix $D$, $HW$, $F$ with `admitted D HW F`, a prime $\ell$, and finite extensions $K$, $L$ of $\mathbb{Q}_\ell$ in $\overline{\mathbb{Q}}_\ell$. Let $K_0$ be the maximal unramified subfield of $K$ and $K_s = K_0(\mu_{\ell^s})$. `Good K s L` means: $s \geq 1$, $s \geq 2$ if $\ell = 2$, $K \subseteq K_s$, and $L$ contains every conjugate of $K_s$. Let $\chi$ be the cyclotomic character.

A *lattice representation* is a continuous $G_K$-action on a finite dimensional $L$-space $V$ with a stable free $\mathcal{O}_L$-lattice $T$ that spans $V$. Let $H^1_f$ be the module of maps $G_K \to V/T$ that reduce a continuous cocycle $c$ with $c \otimes 1$ a coboundary in $V \otimes B$, plus the coboundaries of $V/T$. Here $B$ plays the role of $B_{\mathrm{cris}}$. This is the cocycle form of the [Bloch-Kato group](/learn/galois-cohomology/#selmer-and-tate-shafarevich-groups) $H^1_f(K, V/T)$ (Lean `HfD`).

**Theorem** (`TBat`). Let $e, M_0, h_0 \geq 0$. Let $Y$, $\tilde Y$, $Z$, $V_e$ be lattice representations and $\iota \colon Y \to \tilde Y$, $\pi \colon \tilde Y \to Z$ maps of them. Suppose:

1. $0 \to Y \to \tilde Y \to Z \to 0$ is exact, $\pi$ maps $T_{\tilde Y}$ onto $T_Z$, and $\iota^{-1}(T_{\tilde Y}) \subseteq T_Y$;
2. $\dim Z = 1$ and $G_K$ acts trivially on $Z$;
3. $\dim V_e = 1$ and $G_K$ acts on $V_e$ by $\chi^{-e}$;
4. $\tilde Y$ is crystalline on the subgroup `S.W.GKs` of the Wach data;
5. `HypW`: $Y$ is crystalline on the same subgroup, the jumps of its Hodge filtration lie in $[-M_0, h_0]$, and $Y$ has a Wach-type module with six properties (not unfolded here);
6. $\tilde y \in T_{\tilde Y}$ and $\pi(\tilde y)$ generates $T_Z$;
7. $\varphi \colon T_Y \to V_e/T_e$ is $\mathcal{O}_L$-linear and $G_K$-equivariant;
8. $f \colon G_K \to T_Y$ satisfies $\iota(f(g)) = g\tilde y - \tilde y$.

Then $g \mapsto \ell^{c}\, \varphi(f(g))$ lies in $H^1_f(K, V_e/T_e)$, where
$$c = N + (e+2)s + v_\ell(e) + \lfloor e/(\ell-1) \rfloor + 1 + s + v_\ell(e+1) + g_K,$$
with $g_K = v_\ell[K_s:\mathbb{Q}_\ell] - v_\ell[K:\mathbb{Q}_\ell]$ and $N$ the constant `cLL` of `torsion_bound_of_weight_hyp`.

## Proof

1. `ConnCoc.conn`: $f$ is a cocycle, locally constant modulo each $\ell^n$.
2. `isCoc_tmul_one`: on $G_{K_s}$, $f \otimes 1$ is a continuous cocycle with values in $T_Y \otimes A_{\inf}/\xi^{e+1}$.
3. `ses_lattice_trivial_quotient`: some $\ell^k (f \otimes 1)$ is a coboundary. This uses `adm5`, `adm7` and that $\tilde Y$ is crystalline.
4. `torsion_bound_of_weight_hyp`: with `HypW`, a class killed by a power of $\ell$ is killed by $\ell^N$. So this holds for $k = N$.
5. [`mem_HfD_of_lattice`](/entry/mem-hf-d-of-lattice/) gives the conclusion. It takes local Tate duality (`adm2`) and Tate's Euler characteristic formula.

The rest unfolds `cTBY`.

## In the Lean code

The theorem is at [CrystallineExtensionClassBound.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallineExtensionClassBound.lean#L359). `TBat`, `cTB` and `cTBY` are in [LocalSituation.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalSituation.lean#L165), and `HfD` is in [StatementTor.lean](lean:Formalism/WeaklyAdmissibleFiltrations/StatementTor.lean#L126). We read the statements of the lemmas it calls, not their proofs.

Three hypotheses of `TBat` are never used: $\dim Z = 1$, $\dim V_e = 1$, and that $\pi(\tilde y)$ generates $T_Z$ (line 360). Only four of the nine parts of `admitted` are kept, at line 361. The part named `ArchimedeanSignatureMatching` is in fact Tate's Euler characteristic formula (`LocalEulerCharK`).

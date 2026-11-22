---
id: link-g-without-kernels
title: LinkG for one family, with the chain part set to zero
kind: theorem
decl: Formalism.L2.G.linkG_without_kernels
module: Formalism.LocalToGlobal.GroupLattices.AdmissibleFamilyNoKernel
covers: 564
status: drafted
drafted_by: writer@claude
---
This theorem proves the bound `LinkG` for one family from the nine admissibility conditions and five local facts. Its only user is [LinkG for one family](/entry/link-g-fam-no-ker/), which builds these inputs. The proof replaces the chain part of the lattice instance by zero. Then the valuation clauses of the admissibility hold with no work, and `LinkG` does not see the change.

## Statement

Use the notation of [LinkG from local data](/entry/link-of-local-closed/): $F$ is a family with data $D(x,i)$, size data $L(x,i)$, an instance $G_x(x,i)$, a lattice instance $G_y(x,i)$ and constants $K$. $\mathrm{Ev}_F(P)$ means that $P(x,i)$ holds for all large $x$ and all $i$.

**Theorem.** Assume `Adm1F F` to `Adm9F F`, and assume that eventually:

- each local datum of $D(x,i)$ has trivial stabilisers and finitely many classes;
- the operators of $D(x,i)$ preserve the lattices (`OperatorsPreserveLattices`);
- the orbit lattice bounds `OrbitLatticeBounds` hold for $G_x$ and $G_y$, and the sandwich `LatticeSandwich` holds for $G_x$.

Assume also `NPDescF F`. Then `LinkG F`.

## Proof

Let $G_y^0$ be $G_y$ with each chain replaced by the zero chain (`zeroCh`).

1. `admissible_family_no_kernel` proves the family admissibility `AdmF` for $(G_x, G_y^0)$, and eventually `unitBoundAtTwistedPlaces` and `admG1` for $G_y^0$. The valuation clauses (`vKge`) ask that the image of a vector under the chain lies in a scaled lattice $\varpi^{\lceil g v \rceil} N$. For the zero chain this image is $0$, so they hold for each $g$ (`vKge_zero`). The rest of `admG1` comes from `gluing_statement_holds`, with the four local facts.
2. `AuxBlock8.Pf.stmtF` is proved for every family. With `AdmF` it gives $C$ and $\delta$ with $\delta(x) \to 0$ such that `Conclusion₂` holds eventually, with the bound $b^{\delta(x)}$.
3. `linkG_at_of` turns `Conclusion₂`, `admG1` for $G_y^0$ and four facts on $G_x$ into `LinkG_at` with the constant $4|C| + 1$. The facts are `ServedGIdx`, `SvBound`, `NuServed`, and the lattice lengths of `sizeDataLat_ev`, which uses `NPDescF`.

## In the Lean code

The theorem is at [AdmissibleFamilyNoKernel.lean line 224](lean:Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean#L224). `zeroCh` is at line 166, `vKge_zero` at line 178 and `admissible_family_no_kernel` at line 188. `stmtF` is in [LogarithmicSums.lean](lean:Formalism/SharpRestriction/GrowthBounds/LogarithmicSums.lean#L101), and `linkG_at_of` in [PlaneCountTheoremWithConstants.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCountTheoremWithConstants.lean#L811).

- The zero chain is a shortcut, not a proof of the valuation bounds for $G_y$. This is sound, because `LinkG` reads only $G_x$ and $K$. Lean also accepts the lattice lengths and the tie `latTied`, proved for $G_y$, in the place of the facts for $G_y^0$. So these facts do not read the chain part.
- `admissible_family_no_kernel` takes `NPDescF` and does not use it. The present theorem uses it only for `sizeDataLat_ev`.
- The hypothesis on `OrbitLatticeBounds` is for $G_y$, not $G_y^0$.
